# mypainter 모듈

from tkinter import colorchooser

def get_color():
    color = colorchooser.askcolor() # 선택한 색상 정보를 튜플로 반환
    return color[1]   # 튜플의 두 번째 항목(색상 코드)을 반환

def get_xy(x, y, bold): # 펜 두께(bold)에 따라 타원의 크기 결정
    if bold:
        return (x-4, y-4, x+4, y+4) # 타원의 좌표를 넓게 = 두껍게
    else:
        return (x-2, y-2, x+2, y+2) # 타원의 좌표를 좁게 = 가늘게

