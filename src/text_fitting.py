from PIL import ImageFont
from rectangle import Rectangle

def draw_text_around_rectangle(draw, text, start_x, start_y, end_x, end_y):
    free_space = calculate_free_space(start_x, start_y, end_x, end_y)

    font_size, line_spacing, character_spacing = find_optimal_text_settings(free_space, text)

    font = ImageFont.truetype("arial.ttf", font_size)
    line_height = font.getmetrics()[0]  # Получаем высоту строки шрифта

    # Определяем координаты для отображения текста
    x_offset = free_space.x
    y_offset = free_space.y

    for line in text.split('\n'):
        draw.text((x_offset, y_offset), line, fill="black", font=font)
        y_offset += int(line_height * line_spacing)
    
    return font_size, line_spacing, character_spacing

def calculate_free_space(start_x, start_y, end_x, end_y):
    width = (800 - abs(end_x - start_x)) if ((600 - abs(end_y - start_y)) < 600 // 4) else (800)
    height = (600 - abs(end_y - start_y)) if ((800 - abs(end_x - start_x)) < 800 // 4) else (600)

    return Rectangle(0, 0, width, height)

def find_optimal_text_settings(free_space, text):
    optimal_font_size = 6
    optimal_line_spacing = 1.0
    optimal_character_spacing = 0.0

    best_fit_score = float('inf')
    prev = 0
    counter = 1

    for font_size in range(6, 70):
        for line_spacing in [1.0, 1.15, 1.5, 2.0, 2.5, 3.0]:  # Интервалы между строками
            for character_spacing in [0.0, 1.0, 2.0]:  # Интервалы между символами
                fit_score = calculate_fit_score(free_space, text, font_size, line_spacing, character_spacing)
                if (prev == fit_score): counter += 1
                else: counter = 1

                if (fit_score < best_fit_score):
                    optimal_font_size = font_size
                    optimal_line_spacing = line_spacing
                    optimal_character_spacing = character_spacing
                    best_fit_score = fit_score

                if counter == 10: return optimal_font_size, optimal_line_spacing, optimal_character_spacing
                prev = fit_score

    return optimal_font_size, optimal_line_spacing, optimal_character_spacing

def calculate_fit_score(free_space, text, font_size, line_spacing, character_spacing):
    font = ImageFont.truetype("arial.ttf", size=font_size)
    line_height = font.getmetrics()[0]
    num_lines = min(free_space.height // line_height, len(text.split('\n')))
    text_width = max([font.getbbox(line)[2] for line in text.split('\n')[:num_lines]])

    free_area = free_space.width * free_space.height
    occupied_area = text_width * ((line_height * line_spacing) if (character_spacing == 0.0) else (line_height * line_spacing * character_spacing)) * num_lines

    if (((line_height * line_spacing) if (character_spacing == 0.0) else (line_height * line_spacing * character_spacing)) * num_lines > free_space.height or text_width > free_space.width): fit_score = free_area
    else: fit_score = abs(occupied_area - free_area)

    return fit_score
