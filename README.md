# Wrapture

<p align="center" width="100%">
    <img width="256px" src="./public/wrapture-logo-small.png" alt="wrapture logo" />
</p>

> One-click exporter from PyTorch models to Web-ready ONNX with JS/TS wrappers.

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](http://makeapullrequest.com)
[![SemVer 2.0](https://img.shields.io/badge/SemVer-2.0-green.svg)](http://semver.org/spec/v2.0.0.html)
![npm version](https://img.shields.io/npm/v/wrapture)
![issues](https://img.shields.io/github/issues/phun-ky/wrapture)
![license](https://img.shields.io/npm/l/wrapture)
![size](https://img.shields.io/bundlephobia/min/wrapture)
![npm](https://img.shields.io/npm/dm/wrapture)
![GitHub Repo stars](https://img.shields.io/github/stars/phun-ky/wrapture)
[![codecov](https://codecov.io/gh/phun-ky/wrapture/graph/badge.svg?token=VA91DL7ZLZ)](https://codecov.io/gh/phun-ky/wrapture)
[![build](https://github.com/phun-ky/wrapture/actions/workflows/check.yml/badge.svg)](https://github.com/phun-ky/wrapture/actions/workflows/check.yml)

## About

Wrapture lets you go from a Python-trained model to deployable JavaScript with a
single command. It generates TypeScript bindings and a Web/Node-compatible
wrapper, using WebGPU/WASM-ready ONNX runtimes.

> [!NOTE]
> This is an experiment trying to fulfil a need between python and js.
> YMMV

## Table of Contents<!-- omit from toc -->

- [Wrapture](#-wrapture)
  - [About](#about)
  - [🚀 Features](#-features)
  - [Prerequisites](#prerequisites)
    - [Python 3.10+ required](#python-310-required)
    - [Install required Python packages](#install-required-python-packages)
  - [Installation](#installation)
  - [Generating a Model](#generating-a-model)
  - [Usage](#usage)
  - [Output Structure](#output-structure)
  - [Example: Using the Generated Model](#example-using-the-generated-model)
  - [API](#api)
  - [Contributing](#contributing)
  - [License](#license)
  - [Changelog](#changelog)
  - [Sponsor me](#sponsor-me)

## 🚀 Features

- ✅ Convert PyTorch models to ONNX
- ✅ Optional ONNX simplification and quantization
- ✅ Generate `loadModel()` + `predict()` JavaScript wrappers
- ✅ Auto-generate `.d.ts` TypeScript bindings

---

## Prerequisites

### Python 3.10+ required

Install Python if you don’t have it: 👉 <https://www.python.org/downloads/>

---

### Install required Python packages

```shell-session
python3 -m pip install torch onnx onnxsim onnxruntime
```

Check your installation:

```shell-session
python3 -c "import torch; print(torch.__version__)"
python3 -c "import onnx; print(onnx.__version__)"
```

You should see output like:

`2.x.x` etc..

## Installation

```shell-session
npm i -g wrapture
```

## Generating a Model

A helper script is provided to create a basic test model.

```shell-session
python3 python/scripts/basic_model.py
```

This generates:

```shell-session
test/fixtures/basic_model.pt
```

## Usage

```shell-session
wrapture --input test/fixtures/basic_model.pt --output ./wrapped
```

You’ll see a spinner as the model is converted, and then a JS/TS wrapper is
written to the ./wrapped/ directory.

## Output Structure

Example contents of a `--output ./` folder:

```shell-session
/
 ├── wrapped.ts # The loadModel() + predict() logic
 ├── wrapped.d.ts # Fully typed API
 └── model.onnx # Exported ONNX model
```

## Example: Using the Generated Model

```ts
import { loadModel } from './wrapped.js';

const model = await loadModel();

const input = { data: new Float32Array(1 _3_ 224 \* 224), dims: [1, 3, 224, 224]
};

const result = await model.predict(input); console.log(result); // { // logits:
Float32Array, // probabilities: number[], // predictedClass: number // }
```

---

## API

Full API documentation is available
[here](https://github.com/phun-ky/wrapture/blob/main/api/README.md).

---

## Contributing

Want to contribute? Please read the
[CONTRIBUTING.md](https://github.com/phun-ky/wrapture/blob/main/CONTRIBUTING.md)
and
[CODE_OF_CONDUCT.md](https://github.com/phun-ky/wrapture/blob/main/CODE_OF_CONDUCT.md)

## License

This project is licensed under the MIT License - see the
[LICENSE](https://github.com/phun-ky/wrapture/blob/main/LICENSE) file for
details.

## Changelog

See the
[CHANGELOG.md](https://github.com/phun-ky/wrapture/blob/main/CHANGELOG.md) for
details on the latest updates.

## Sponsor me

I'm an Open Source evangelist, creating stuff that does not exist yet to help
get rid of secondary activities and to enhance systems already in place, be it
documentation or web sites.

The sponsorship is an unique opportunity to alleviate more hours for me to
maintain my projects, create new ones and contribute to the large community
we're all part of :)

[Support me on GitHub Sponsors](https://github.com/sponsors/phun-ky).
