# 像素画生成器

## 使用方法

先编辑`config.json`文件，`level`表示像素画的层级，越高其颜色层级越少。`zoom_level`表示缩放比例，`zoom_level`越大，生成的像素画越模糊。

```console
python main.py <input> <output>
```

`<input>` 表示输入文件地址，`<output>` 表示输出文件地址。

## 示例

```console
python main.py input.png output.png
```

## 原理

在图片文件中分为RGB三个通道，以其中任意一个通道为例。将该通道的某一像素值转化成八位二进制数，高位的数字所含信息代表了图像的轮廓，低位信息表示了图像的细节。我们把低位信息全部抹除，这样的话图片中的大致轮廓保留了下来，颜色的层级也降低了，符合像素画的低颜色层级风格。

在处理图片前，先将图片缩小一定倍率，处理过后再放大，这样产生的像素画更有风格。

## 效果

处理前：
![图 0](images/e77d023267d3bfa281e92b8d8a2673cb9872f0776601b63ccfe1210ce0a21c74.png)  

处理后：
![图 1](images/4f3aee03ea512c36201ed96a1c882c4c82765326e7e725e49eebc82ef7d23665.png)  
