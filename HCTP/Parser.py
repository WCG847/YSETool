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

    def aggregate_stats(self):
        self.YFILE.seek(self.YSKILL)
        YPOINT = int.from_bytes
        YSLIST = []

        def YSBS(YDATA):
            return YPOINT(YDATA, 'little') >> 1

        for _ in range(self.YSKILLSIZE):
            YSTR = YSBS(self.YFILE.read(1))
            YSUB = YSBS(self.YFILE.read(2))
            YENDURE = YSBS(self.YFILE.read(3))
            YTECH = YSBS(self.YFILE.read(4))
            YSPD = YSBS(self.YFILE.read(5))

            YSLIST.append({
                'Strength': YSTR,
                'Submission': YSUB,
                'Endurance': YENDURE,
                'Technique': YTECH,
                'Speed': YSPD,
            })

        return YSLIST
