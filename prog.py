# -*- coding: utf-8 -*- 
for i in list:
        if (i.xpos, i.ypos) == (x, y):
            x, y = apple_gen(list)
        else:
            continue
    return x, y


apple.xpos, apple.ypos = apple_gen(list)  # начальное положение яблока
while done:
    some_x = list[
        len(list) - 1].xpos  # если бедет захвачено яблоко, добавленной части хвоста передаётся это значение по Х
    some_y = list[len(list) - 1].ypos  # --//-- по У
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            # Выясняем какая именно кнопка была нажата
            if event.key == pygame.K_LEFT:
                going = 'left'
            if event.key == pygame.K_RIGHT:
                going = 'right'
            if event.key == pygame.K_UP:
                going = 'up'
            if event.key == pygame.K_DOWN:
                going = 'down'
    do_going(going)  # передаем новые координаты змейки
    # если съедено яблоко
    if list[0].xpos == apple.xpos and list[0].ypos == apple.ypos:
        counter += 1
        list.append(Zmey(some_x, some_y, 'element.jpg'))
        apple.xpos, apple.ypos = apple_gen(list)
    screen.fill((0, 0, 0))
    draw_setka()
    # отрисовка змейки через цикл
    for i in list:
        i.render()
    apple.render()
    asd.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(300)
