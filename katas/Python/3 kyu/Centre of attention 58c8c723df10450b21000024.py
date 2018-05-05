# https://www.codewars.com/kata/58c8c723df10450b21000024
class Central_Pixels_Finder(Image):

    def update_pixel(self, idx, depth, last, me=False):
        if self.pixels[idx - self.width] != self.colour or self.pixels[idx + self.width] != self.colour:
            self.depth_map[idx] = 1
        else:
            self.depth_map[idx] = min(
                depth, last + 1, self.depth_map[idx] if me else depth,
                self.depth_map.get(idx - self.width, depth) + 1, self.depth_map.get(idx + self.width, depth) + 1
            )
        return self.depth_map[idx]
            
    def process_segment(self, begin, end):
        middle = begin + (end - begin) // 2 + 1
        last = depth = 1
        for idx in range(begin, middle):
            last = self.update_pixel(idx, depth, last)
            depth += 1

        depth -= 1 + (end - begin + 1) % 2
        for idx in range(middle, end + 1):
            last = self.update_pixel(idx, depth, last)
            depth -= 1

    def process_segment_reverse(self, begin, end):
        middle = begin + (end - begin) // 2 + 1
        last = depth = 1
        for idx in range(end, middle - 1, -1):
            last = self.update_pixel(idx, depth, last, True)
            depth += 1

        depth += 1 + (end - begin + 1) % 2
        for idx in range(middle - 1, begin - 1, -1):
            last = self.update_pixel(idx, depth, last, True)
            depth -= 1

    def central_pixels(self, colour):
        self.depth_map = {}
        self.colour = colour

        for i in range(0, self.width):
            if self.pixels[i] == colour:
                self.depth_map[i] = 1
            idx = len(self.pixels) - 1 - i
            if self.pixels[idx] == colour:
                self.depth_map[idx] = 1

        for i in range(self.width, len(self.pixels) - self.width, self.width):
            begin = end = None
            for col, j in enumerate(range(i, i + self.width)):
                if self.pixels[j] == colour:
                    if begin is None:
                        begin = end = j
                    else:
                        end = j
                elif begin is not None:
                    self.process_segment(begin, end)
                    begin = end = None
            if begin is not None:
                self.process_segment(begin, end)

        for i in range(len(self.pixels) - 2 * self.width, self.width, -self.width):
            begin = end = None
            for j in range(i + self.width - 1, i - 1, -1):
                if self.pixels[j] == colour:
                    if end is None:
                        begin = end = j
                    else:
                        begin = j
                elif end is not None:
                    self.process_segment_reverse(begin, end)
                    begin = end = None
            if end is not None:
                self.process_segment_reverse(begin, end)

        result = []
        if self.depth_map:
            depth_map = sorted(self.depth_map.items(), key=lambda x: x[1], reverse=True)
            max_depth = depth_map[0][1]
            for idx, depth in depth_map:
                if depth == max_depth:
                    result.append(idx)
        return result