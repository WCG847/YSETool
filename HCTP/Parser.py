class YSTAT:
    YSKILL = 0X00
    YSKILLSIZE = 5
    YSSKILL = 0X08
    YMOVE = 0X10
    YMOVESIZE = 258
    YROSTER = 0X112
    CHAR_LIMIT = 22

    def __init__(self, file_path=None):
        self.file_path = file_path
        self.YFILE = open(self.file_path, 'rb')
        self.YPOINT = int.from_bytes

    def aggregate_stats(self):
        self.YFILE.seek(self.YSKILL)
        YSLIST = []
        YSSLIST = []

        def YSBS(YDATA):
            return self.YPOINT(YDATA, 'little') >> 1

        def parse_stats():
            YSTR = YSBS(self.YFILE.read(1))
            YSUB = YSBS(self.YFILE.read(1))
            YENDURE = YSBS(self.YFILE.read(1))
            YTECH = YSBS(self.YFILE.read(1))
            YSPD = YSBS(self.YFILE.read(1))
            return {
                'Strength': YSTR,
                'Submission': YSUB,
                'Endurance': YENDURE,
                'Technique': YTECH,
                'Speed': YSPD,
            }

        for _ in range(self.YSKILLSIZE):
            YSLIST.append(parse_stats())

        self.YFILE.seek(self.YSSKILL)

        for _ in range(self.YSKILLSIZE):
            YSSLIST.append(parse_stats())

        return YSLIST, YSSLIST


