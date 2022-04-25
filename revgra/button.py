import pygame

class Button:
    def __init__(self, bx=0, by=0, bw=200, bh=50, color=(255, 255, 255)):
        # about button
        self._is_active = True
        self._is_visible = True
        self._is_bg_visible = True
        self._bx, self._by, self._bw, self._bh = bx, by, bw, bh
        self._color = color
        self._margin = 10
        self._layout = 0

        # about text
        self._hasText = False
        self._tx, self._ty = 0, 0

        # about icon
        self._hasIcon = False
        self._ix, self._iy, self._iw, self._ih = 0, 0, 30, 30

        self._update()

    # about general
    def get_center(self):
        return (self._bx+self._bw//2, self._by+self._bh//2)


    def __contains__(self, pos):
        if not self._is_active: return False
        if not (self._bx < pos[0] <= self._bx + self._bw): return False
        if not (self._by < pos[1] <= self._by + self._bh): return False
        return True

    def set_position(self, bx, by):
        self._bx, self._by = bx, by
        self._update()

    def set_size(self, bw, bh):
        self._bw, self._bh = bw, bh
        self._update()

    def set_color(self, c):
        self._color = c

    def set_active(self, b=True):
        self._is_active = b

    def set_visible(self, b=True):
        self._is_visible = b

    def set_bg_visible(self, b=True):
        self._is_bg_visible = b

    def set_margin(self, margin):
        self._margin = margin
        self._update()

    def set_layout_center(self):
        self._layout = 0
        self._update()

    def set_layout_left(self):
        self._layout = 1
        self._update()

    # about text
    def set_text(self, text, color=(0, 0, 0), size=40, font=None, bold=False):
        self._text = text
        self._textColor = color
        self._textSize = size
        self._font = font
        self._isBold = bold
        self._hasText = True
        self._update()

    def set_textColor(self, color):
        self._textColor = color
        self._update()

    def set_textSize(self, size):
        self._textSize = size
        self._update()

    def set_font(self, font):
        self._font = font
        self._update()

    def set_bold(self, bold=True):
        self._isBold = bold
        self._update()

    # about icon
    def set_icon(self, path):
        try:
            self._icon = pygame.image.load(path)
            self._hasIcon = True
            self._update()
        except:
            print(f"'{path}' was not found.")

    def set_iconSize(self, iw, ih):
        self._iw, self._ih = iw, ih
        self._update()

    # about general
    def _update(self):
        self._preparation()
        text_offset = [0, 0]
        icon_offset = [0, 0]

        if self._hasIcon:
            icon_offset = self._pyIcon.get_rect(center=(self._bw//2, self._bh//2))
        if self._hasText and self._hasIcon:
            text_offset = self._pyText.get_rect(center=((self._bw-self._iw-self._margin)//2, self._bh//2))
        if self._hasText and not self._hasIcon:
            text_offset = self._pyText.get_rect(center=(self._bw//2, self._bh//2))

        self._iy = icon_offset[1] + self._by
        self._ty = text_offset[1] + self._by

        if self._hasIcon and not self._hasText:
            self._ix = icon_offset[0] + self._bx

        if self._layout == 0:  # center
            if self._hasText and self._hasIcon:
                self._ix = self._bx + self._margin
                self._tx = text_offset[0] + self._bx + self._iw
            else:
                self._tx = text_offset[0] + self._bx

        if self._layout == 1:  # left
            if self._hasText and self._hasIcon:
                self._ix = self._bx + self._margin
                self._tx = self._iw + self._bx + self._margin + self._margin
            else:
                self._tx = self._bx + self._margin

        self._preparation()

    def _preparation(self):
        self._pyBox = pygame.Rect(self._bx, self._by, self._bw, self._bh)
        if self._hasText:
            pyfont = pygame.font.SysFont(self._font, self._textSize, bold=self._isBold)
            self._pyText = pyfont.render(self._text, True, self._textColor)
        if self._hasIcon:
            self._pyIcon = pygame.transform.scale(self._icon, (self._iw, self._ih))

    def draw(self, screen):
        if not self._is_visible: return
        if self._is_bg_visible: pygame.draw.rect(screen, self._color, self._pyBox)
        if self._hasText: screen.blit(self._pyText, (self._tx, self._ty))
        if self._hasIcon: screen.blit(self._pyIcon, (self._ix, self._iy))
