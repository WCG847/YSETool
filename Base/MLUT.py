class HCTPSVR:
    YMOVE = 0X10
    YMOVESIZE = 258

    def __init__(self, file_path=None):
        self.file_path = file_path
        self.YFILE = open(self.file_path, 'rb')
        self.YINT = int.from_bytes

    def GetLUT(self):
        self.YFILE.seek(self.YMOVE)
        YMIDX = []

        def YI(YDATA):
            return self.YINT(YDATA, 'little')

        def parse_LUT():
            YBYTE = 2
            keys = ['YFS', 'YT1', 'YT2', 'YT3', 'YT4', 'YT5', 'YT6', 'YT7', 'YT8', 'YT9', 'YT10', 'YT11', 'YT12', 'YT13']
            values = [YI(self.YFILE.read(YBYTE)) for _ in keys]
            return dict(zip(keys, values))
