from PIL import Image
from io import StringIO
# import dynamic_quality

im = Image.open("26-20210402080043.jpg")
print(im.format, im.size, im.mode)

new_photo = im.copy()
new_photo.thumbnail(im.size, resample=Image.ANTIALIAS)
save_args = {'format': im.format}
if im.format == 'JPEG':
    save_args['quality'].value = 85
    # 开启optimize设置，这是以CPU耗时为代价节省额外的文件大小
    save_args['optimize'] = True
    # 渐进式： JPEG 图片从模糊到清晰载入。
    # 渐进式的选项可以在 Pillow 中轻松的启用 (progressive=True)。
    # 渐进式文件的被打包时会有一个小幅的压缩。
    save_args['progressive=True'] = True

new_photo.save("copy-26-20210402080043.jpg", **save_args)
