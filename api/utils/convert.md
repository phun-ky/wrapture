[wrapture](../README.md) / utils/convert

# utils/convert

> Last updated 2025-06-16T18:17:10.527Z

## Interfaces

### ConvertOptionsInterface

Defined in:
[utils/convert.ts:12](https://github.com/phun-ky/wrapture/blob/main/src/utils/convert.ts#L12)

Options for the [convert](#convert) function.

#### Properties

| Property                          | Type      | Description                                                                                   | Defined in                                                                                    |
| --------------------------------- | --------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| <a id="format"></a> `format?`     | `string`  | The output format for the converted model (e.g., 'onnx'). Defaults to 'onnx' if not provided. | [utils/convert.ts:17](https://github.com/phun-ky/wrapture/blob/main/src/utils/convert.ts#L17) |
| <a id="quantize"></a> `quantize?` | `boolean` | Whether to apply quantization to the model.                                                   | [utils/convert.ts:22](https://github.com/phun-ky/wrapture/blob/main/src/utils/convert.ts#L22) |

## Functions

### convert()

```ts
function convert(inputPath, outputDir, opts): Promise<void>;
```

Defined in:
[utils/convert.ts:49](https://github.com/phun-ky/wrapture/blob/main/src/utils/convert.ts#L49)

Converts a machine learning model to ONNX or another supported format by
delegating to a Python script (`convert.py`).

This function spawns a subprocess using `python3` and monitors stdout/stderr. It
supports additional options such as format selection and quantization.

convert

#### Parameters

| Parameter   | Type                                                  | Description                                         |
| ----------- | ----------------------------------------------------- | --------------------------------------------------- |
| `inputPath` | `string`                                              | Path to the input model file                        |
| `outputDir` | `string`                                              | Directory where the converted model should be saved |
| `opts`      | [`ConvertOptionsInterface`](#convertoptionsinterface) | Conversion options                                  |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

A promise that resolves on success or rejects if conversion fails

#### Throws

If the Python process exits with a non-zero code

#### Example

```ts
await convert('models/model.pt', 'out/', { format: 'onnx', quantize: true });
```

#### See

- https://nodejs.org/api/child\_process.html#child\_processspawncommand-args-options
- https://github.com/sindresorhus/ora - Ora spinner for CLI feedback
- https://github.com/chalk/chalk - Chalk for terminal coloring

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
