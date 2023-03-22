class Emulate:
    def __init__(self):
        self.data = ['jpg', 'png', 'jp2', 'bmp', 'gif', 'tiff', 'webp', 'jpeg']
        self.error_not_num = "输入的图片标签不可读"
        self.error_null = "缺少输入的图片标签"
        self.error_beyone_num = "输入的图片标签超过范围"

    def get_labels(self, _):
        if _ is None:
            return self.error_null
        if not _.isdigit():
            return self.error_not_num
        if not int(_) >= len(self.data):
            return self.error_beyone_num
        return self.data[int(_)]
