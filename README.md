# ПРАКТИКУМ ПО ПРОГРАММИРОВАНИЮ (1 курс)

## ВТОРОЙ СЕМЕСТР

## ЗАДАНИЕ 2. Реализация пакета модулей для манипулирования плоскими фигурами.

## Работу выполнил студент группы ТРПО24-3 Третьяк Александр Олегович



Реализовать API, которое позволяет генерировать, преобразовывать и визуализировать последовательность плоских полигонов, представленных в виде картежа картежей (например: ((0,0), (0,1), (1,1), (1,0)) — представление для квадрата). Последовательности представлений полигонов представляют собой итераторы (далее: последовательности полигонов). Решать задачи с использованием функционального стиля программирования, в том числе активно использовать функции из модуля itertools и functools.

Суммарная сложность дополнительных заданий должна быть не менее 5.

    Реализовать функцию визуализации последовательности полигонов, представленной в виде итератора (например, можно использовать визуализацию с помощью библиотеки matplotlib, см. пример: ссылка).


    Реализовать функции, генерирующие бесконечную последовательность непересекающихся полигонов с различающимися координатами (например, «ленту», см. рис. 2):

    прямоугольников (gen_rectangle);

    треугольников (gen_triangle);

    правильных шестиугольников (gen_hexagon).

    с помощью данных функций используя функции из модуля itertools сгенерировать семь фигур, включающих как прямоугольники, так и треугольники и шестиугольники, визуализировать результат.


    Реализовать операции:

    параллельный перенос (tr_translate);

    поворот (tr_rotate);

    симметрия (tr_symmetry);

    гомотетия (tr_homothety);

которые можно применить к последовательности полигонов с помощью функции map.


    С помощью данных функций создать и визуализировать (рис. 3):

    три параллельных «ленты» из последовательностей полигонов, расположенных под острым углом к оси абсцисс;

    две пересекающихся «ленты» из последовательностей полигонов, пересекающихся не в начале координат;

    две параллельных ленты треугольников, ориентированных симметрично друг к другу;

    последовательность четырехугольников в разном масштабе, ограниченных двумя прямыми, пересекающимися в начале координат.


    Реализовать операции:

    фильтрации фигур, имеющих хотя бы один угол, совпадающий с заданной точкой (flt_angle_point);

    фильтрации фигур, имеющих кратчайшую сторону меньше заданного значения (flt_short_side);

которые можно применить к последовательности полигонов с помощью функции filter.


    С помощью данных функций реализовать и визуализировать:

    фильтрацию фигур, созданных в рамках пункта 4.4; подобрать параметры так, чтобы на выходе было получено шесть фигур;
    

    Реализовать декораторы и продемонстрировать корректность их работы:

    преобразующие многоугольники в итераторах среди аргументов функции, работающие на основе функций из п. 3: @tr_translate, @tr_rotate, @tr_symmetry, @tr_homothety.



