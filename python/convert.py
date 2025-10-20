import argparse
import torch
import torch.nn as nn
import os
from onnxsim import simplify
import onnx
from onnxruntime.quantization import quantize_dynamic, QuantType

def convert_to_onnx(input_path, output_path, quantize=False):
    class BasicCNN(nn.Module):  # Define the same model architecture
        def __init__(self):
            super().__init__()
            self.net = nn.Sequential(
                nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1),
                nn.ReLU(),
                nn.AdaptiveAvgPool2d((1, 1)),
                nn.Flatten(),
                nn.Linear(16, 10)
            )

        def forward(self, x):
            return self.net(x)

    model = BasicCNN()

    model.load_state_dict(torch.load(input_path, map_location='cpu', weights_only=False))

    model.eval()

    dummy_input = torch.randn(1, 3, 224, 224)
    output_model_path = os.path.join(output_path, 'model.onnx')
    torch.onnx.export(
        model,
        dummy_input,
        output_model_path,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}},
        opset_version=11,
        dynamo=False
    )
    model = onnx.load(output_model_path)
    model_simp, check = simplify(model)
    assert check, "Simplified model could not be validated"
    onnx.checker.check_model(model_simp)  # throw if broken
    onnx.save(model_simp, output_model_path)
    print("✓ ONNX model simplified.")

    print(f"✓ Exported ONNX model to: {output_model_path}")

    if quantize:
        quant_model_path = os.path.join(output_path, 'model_quant.onnx')
        quantize_dynamic(output_model_path, quant_model_path, weight_type=QuantType.QInt8)

def main():
    parser = argparse.ArgumentParser(description='Wrapture: Convert PyTorch model to ONNX.')
    parser.add_argument('--input', required=True, help='Path to the PyTorch model (.pt)')
    parser.add_argument('--output', required=True, help='Directory to save the ONNX model')
    parser.add_argument('--format', default='onnx', help='Export format (currently only supports ONNX)')
    parser.add_argument('--quantize', action='store_true', help='Apply quantization')

    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    if args.format.lower() == 'onnx':
        convert_to_onnx(args.input, args.output, args.quantize)
    else:
        raise ValueError(f"Unsupported format: {args.format}")

if __name__ == '__main__':
    main()
