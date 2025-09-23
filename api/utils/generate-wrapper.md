[wrapture](../README.md) / utils/generate-wrapper

# utils/generate-wrapper

> Last updated 2025-09-23T05:22:34.006Z

## Interfaces

### GenerateWrapperOptionsInterface

Defined in:
[utils/generate-wrapper.ts:10](https://github.com/phun-ky/wrapture/blob/main/src/utils/generate-wrapper.ts#L10)

Options for generating ONNX wrapper files.

#### Properties

| Property                       | Type     | Description                                                                                                                                                                      | Defined in                                                                                                      |
| ------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| <a id="backend"></a> `backend` | `string` | The backend to use for inference. This affects the model file used. If set to `'wasm'`, the generated wrapper will load `model_quant.onnx`, otherwise it will load `model.onnx`. | [utils/generate-wrapper.ts:16](https://github.com/phun-ky/wrapture/blob/main/src/utils/generate-wrapper.ts#L16) |

## Functions

### generateWrapper()

```ts
function generateWrapper(outputDir, opts): Promise<void>;
```

Defined in:
[utils/generate-wrapper.ts:40](https://github.com/phun-ky/wrapture/blob/main/src/utils/generate-wrapper.ts#L40)

Generates a TypeScript wrapper and type definition file (`wrapped.ts` and
`wrapped.d.ts`) for use with `onnxruntime-web`, including utility functions like
`softmax`, `argmax`, and a typed `predict()` function.

The generated code loads the correct ONNX model based on the provided backend.

#### Parameters

| Parameter   | Type                                                                  | Description                                            |
| ----------- | --------------------------------------------------------------------- | ------------------------------------------------------ |
| `outputDir` | `string`                                                              | The directory where the wrapper files will be written. |
| `opts`      | [`GenerateWrapperOptionsInterface`](#generatewrapperoptionsinterface) | Wrapper generation options, including backend type.    |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

A Promise that resolves when the wrapper files are successfully written.

#### Throws

Will throw an error if file writing fails.

#### Example

```ts
await generateWrapper('./dist', { backend: 'wasm' });
// Creates `wrapped.ts` and `wrapped.d.ts` in ./dist
```

#### See

https://www.npmjs.com/package/onnxruntime-web

---

**Contributing**

Want to contribute? Please read the
[CONTRIBUTING.md](https://github.com/phun-ky/wrapture/blob/main/CONTRIBUTING.md)
and
[CODE_OF_CONDUCT.md](https://github.com/phun-ky/wrapture/blob/main/CODE_OF_CONDUCT.md)

**Sponsor me**

I'm an Open Source evangelist, creating stuff that does not exist yet to help
get rid of secondary activities and to enhance systems already in place, be it
documentation or web sites.

The sponsorship is an unique opportunity to alleviate more hours for me to
maintain my projects, create new ones and contribute to the large community
we're all part of :)

[Support me on GitHub Sponsors](https://github.com/sponsors/phun-ky).

---

This project created by [Alexander Vassbotn Røyne-Helgesen](http://phun-ky.net)
is licensed under a [MIT License](https://choosealicense.com/licenses/mit/).
