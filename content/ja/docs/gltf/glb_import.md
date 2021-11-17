---
title: "Glbインポート"
date: 2020-10-12T17:04:00+09:00
weight: 1
tags: ["gltf"]
---

# import

glb ファイルを Unity の Assets 下のフォルダに投入すると、glb を Asset 化できます。

## import option
### `ReverseAxis` 反転軸の設定

glTFの右手系Y-UP から Unityの左手系Y-UP に変換するときに反転する軸を選択できます。

* Z軸 (v0.68.0 より前と同じ)
* X軸 (v0.68.0 から追加)

{{< img width=400 src="images/unigltf/glb_axis.gif" >}}

選択して `Apply` を押すと反映されます。

## glb の extract

https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/DamagedHelmet/glTF-Binary

### clear

初期状態(clear)では、関連する Asset (Mesh, Material, Texture, AnimationClip)は SubAsset として配下にあります。

* `texture_1.metallicRoughness` は、`texture_1` を元に Unity の Standard Shader 向けに変換したものです。md" >}})
* `texture_3.occlusion` は、 `textrue_3` を元に Unity の Standard Shader 向けに変換したものです。
* `texture_4.normal` は、 `textrue_4` を元に Unity の Standard Shader 向けに変換したものです。

{{< img width=400 src="images/unigltf/glb_clear.jpg" >}}

### extract

`Extract Materials and Textures ...` を押すと下記のように変化します。

* `Material_MR.mat` の生成
* `texture_0.jpg` の生成(color)
* `texture_1.metallicRoughness.png` の生成。`texture_1` を元に Unity の Standard Shader 向けに変換したものです。
* `texture_2.jpg` の生成(emission)
* `texture_3.occlusion.png` の生成。`textrue_3` を元に Unity の Standard Shader 向けに変換したものです。
* `texture_4.jpg` の生成(normalMap)

{{< img width=400 src="images/unigltf/glb_extract.jpg" >}}

## gltf の extract

https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/DamagedHelmet/glTF

### clear

初期状態(clear)では、関連する Asset (Mesh, Material, Texture(変換が必要なもの), AnimationClip)は SubAsset として配下にあります。

* `Default_AO.occlusion` は、 `Default_AO` を元に Unity の Standard Shader 向けに変換したものです。
* `Defualt_metalRoughness.metallicRoughness` は、`Defualt_metalRoughness` を元に Unity の Standard Shader 向けに変換したものです。

{{< img width=400 src="images/unigltf/gltf_clear.jpg" >}}

### extract

`Extract Materials and Textures ...` を押すと下記のように変化します。

* `Material_MR.mat` の生成
* `Default_AO.occlusion.png` の生成。`Default_AO` を元に Unity の Standard Shader 向けに変換したものです。
* `Default_metalRoughness.metallicRoughness.png` の生成。`Default_metalRoughness` を元に Unity の Standard Shader 向けに変換したものです。

{{< img width=400 src="images/unigltf/gltf_extract.jpg" >}}

## AssetFile の作られ方

### 以前の動作(独立したasset)

VRM0 とv0.67以前のGLB/GLTF の Importerは、以下のように import されます。

{{% alert title="vrm0 の import" color="warning" %}}

{{< img width=300 src="images/vrm10/vrm0_import.jpg" >}}

* mesh や texture や material や blendshape などの関連アセットファイルが作成されます。

{{% /alert %}}

### 新しい動作(subasset)

VRM1 とv0.68以降のGLB/GLTF の Importerは、以下のように import されます。

{{% alert title="vrm1 の import" color="warning" %}}

{{< img width=300 src="images/vrm10/vrm1_import.jpg" >}}

* mesh や material や texture や Expression が SubAsset として作成されます。

{{% /alert %}}

{{% alert title="glb の import" color="warning" %}}

{{< img width=600 src="images/gltf/glb_extract_before.jpg" >}}

* material と texture が SubAsset として作成されます

{{% /alert %}}

## SubAsset を変更するには Extract する

新しい Importer で作られた SubAsset は 内容を変更ができません。

{{% alert title="subasset" color="warning" %}}

SubAsset は VRM 内のリソースを表しているためで、
例えば Material を変更しても、その変更を即座に VRM に反映することができないためです。

FBX の Importer も同様の動作です。

{{% /alert %}}

VRM1 とv0.68以降のGLB/GLTF では、Material タブなどで extract ができます。

{{< img width=300 src="images/vrm10/extract_material.jpg" >}}
{{< img width=300 src="images/vrm10/extract_vrm_empty.jpg" >}}
{{< img width=300 src="images/vrm10/extract_vrm.jpg" >}}

{{% alert title="fbx の extract" color="warning" %}}

fbx importer の material タブには下記のようなボタンがあります。

{{< img src="images/vrm10/fbx_extract.jpg" >}}

`Export Textures...` や `Export Materials...` すると fbx の中の material を 外にコピーして独立した Asset とすることができます。
このコピーされた Asset は自由に変更することができます。

{{% /alert %}}

## 外部の Asset と VRM を関連付ける Remap

初期状態では vrm 内部の Asset が使用されますが、これを外部の Asset と置き換えることができます。
置き換えの関連付けを管理するのが Remap です。

* None になっているときは、 `vrm`, `glb` に内部の SubAsset を使用しているという意味になります。
* Extract以外にも、個別に既存のAssetを割り当てできます

{{% alert title="extract 後" color="warning" %}}

{{< img width=300 src="images/vrm10/remap_materials.jpg" >}}

{{< img width=700 src="images/gltf/glb_extract_after.jpg" >}}

{{< img width=700 src="images/gltf/vrm1_extract_after.jpg" >}}

SubAsset が書き出され、それが Remap に代入されます。

{{% /alert %}}