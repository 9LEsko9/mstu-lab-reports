#set text(font: "Times New Roman", size: 14pt, lang: "Rus")
#set page(paper: "a4", margin: (left: 3cm, right: 1.5cm, top: 2cm, bottom: 2cm))

#let studentName = text(
  style: "italic",
  [
  Оскорбин О.В.
  ],
)

#let proffesorName = text(
  style: "italic",
  [
  Соломахо К. Г.
  ],
)

#let studentGroup = "ИДБ-24-03"

#let studentDeparment = [
  Институт \
  #underline("информационных технологий")
]

#let subjectDeparment = [
  Кафедра \
  #underline([физики])
]

// Header section
#align(center)[
  #strong[
    МИНОБРНАУКИ РОССИИ \
    федеральное государственное автономное образовательное учреждение \
    высшего образования \
    «Московский государственный технологический университет \
    «СТАНКИН»» \
    (ФГАОУ ВО «МГТУ «СТАНКИН»)
  ]
]

// Department table
#table(
  stroke: (top: 0.5pt, rest: none),
  columns: (1fr, 1fr),
  rows: (2cm),
  align: (left, right),
  subjectDeparment,
  studentDeparment
)

// Main content - simplified structure
#v(1fr) // Push content down

#align(center)[
  #strong[
    ЛАБОРАТОРНАЯ РАБОТА №2 \
    #text(size: 12pt)[

      «ИЗМЕРЕНИЕ ПЕРИОДА ДИФРАКЦИОННОЙ РЕШЁТКИ» \

по дисциплине «Физика»

    ]
  ]

  #v(1fr)

  #grid(
    gutter: 1cm,
    [Выполнил студент группы #studentGroup: #h(1fr) #underline(" " * 24 + [/] + studentName)],
    [Проверил: #h(1fr) #underline(" " * 24 + [/] + proffesorName)]
  )
]


#v(1fr) // Push footer down

#align(center)[
  Москва 2026г.
]

#pagebreak()

#set page(numbering: "1", number-align: center + bottom)

#show heading: set text(14pt, weight: "bold")
#show heading: it => {
  it
  v(0.3em)
}

#set par(
  first-line-indent: 1.25cm,
  leading: 1.5em,
  spacing: 1.5em,
  justify: true,
)

#align(center,
  strong("Измерение периода дифракционной решётки")
)

#v(1em)

#text(strong[Цель работы: ] + "ознакомление с явлением дифракции света и использованием его для измерения периода дифракционной решётки." )

#v(0.5cm)

*Краткая теория:*

#v(0.5cm)

Период голографической дифракционной решётки $d$ определяется из условия главных максимумов:

#v(0.5cm)

#grid(
  columns: (1fr, auto, 1fr),
  [],
  $d sin theta_m = m lambda, quad m = 0, plus.minus 1, plus.minus 2, ...$,
  align(right + horizon)[(1)]
)

#v(0.5cm)

где $lambda$ — длина волны, $m$ — порядок максимума, $theta_m$ — угол дифракции. Синус угла вычисляется через измеренные расстояния: $sin theta_m = r_m \/ sqrt(r_m^2 + L^2)$, где $r_m$ — расстояние от нулевого максимума до максимума порядка $m$ на экране, $L$ — расстояние от решётки до экрана.

#pagebreak()

#par([])

*Выполнение работы:*

#v(0.5cm)

Собираем установку по схеме рис. 1. Юстировка: лазерный луч без решётки попадает в центр шкалы экрана; после установки решётки добиваемся перпендикулярности её плоскости лучу.

#v(0.5cm)

#align(center)[
  #image("images/img_0.png", width: 80%)
  Рисунок 1 — Схема измерительной установки: 1 — полупроводниковый лазер, \ 2 — голографическая дифракционная решетка, 3 — экран наблюдения
]

#v(0.5cm)

#pagebreak()

*Выполнение измерений:*

#v(0.5cm)

Для четырёх значений $L$ (0.15; 0.20; 0.25; 0.30 м) измеряем $r_m$ для порядков $m = 1$ и $m = 2$. Вычисляем $sin theta_m$ и $d = m lambda \/ sin theta_m$. Относительная погрешность каждого измерения:

#align(center)[
  $epsilon = display(Delta d / d) = display(L^2 / (r_m^2 + L^2)) lr((display(Delta L / L) + display(Delta r_m / r_m)))$
]

Приборная погрешность линейки: $Delta L = Delta r_m = 1$ мм. Результаты — в таблице 1.

#pagebreak()

#par([])

*Таблица 1* — Результаты измерений периода дифракционной решётки

#table(
  columns: (auto, auto, auto, auto, auto, auto, auto),
  rows: (0.8cm),
  align: horizon + center,
  [*№*], [*$L$, м*], [*$m$*], [*$r_m$, м*], [*$sin theta_m$*], [*$d$, мкм*], [*$Delta d$, мкм*],
  [1],  [0.15], [1], [0.063], [0.38723], [1.679], [0.032],
  [2],  [0.15], [2], [0.187], [0.78005], [1.667], [0.008],
  [3],  [0.20], [1], [0.085], [0.39114], [1.662], [0.024],
  [4],  [0.20], [2], [0.249], [0.77965], [1.667], [0.006],
  [5],  [0.25], [1], [0.106], [0.39036], [1.665], [0.019],
  [6],  [0.25], [2], [0.311], [0.77940], [1.668], [0.005],
  [7],  [0.30], [1], [0.127], [0.38984], [1.667], [0.016],
  [8],  [0.30], [2], [0.374], [0.78005], [1.667], [0.004],
  [СР], [—],   [—], [—],     [—],       [1.668], [0.014]
)

#v(1cm)

#pagebreak()

*Обработка результатов:*

#v(0.5cm)

Для каждого измерения вычисляем $d_i = display(m lambda / sin theta_m)$:

#v(0.25cm)

#v(0.25cm)
#block[$d_1 = display(1 times 6.5 times 10^(-7) / 0.38723) approx 1.679$ мкм $= 1.679 times 10^(-6)$ м]
#v(0.4cm)
#block[$d_2 = display(2 times 6.5 times 10^(-7) / 0.78005) approx 1.667$ мкм $= 1.667 times 10^(-6)$ м]
#v(0.4cm)
#block[$d_3 = display(1 times 6.5 times 10^(-7) / 0.39114) approx 1.662$ мкм $= 1.662 times 10^(-6)$ м]
#v(0.4cm)
#block[$d_4 = display(2 times 6.5 times 10^(-7) / 0.77965) approx 1.667$ мкм $= 1.667 times 10^(-6)$ м]
#v(0.4cm)
#block[$d_5 = display(1 times 6.5 times 10^(-7) / 0.39036) approx 1.665$ мкм $= 1.665 times 10^(-6)$ м]
#v(0.4cm)
#block[$d_6 = display(2 times 6.5 times 10^(-7) / 0.77940) approx 1.668$ мкм $= 1.668 times 10^(-6)$ м]
#v(0.4cm)
#block[$d_7 = display(1 times 6.5 times 10^(-7) / 0.38984) approx 1.667$ мкм $= 1.667 times 10^(-6)$ м]
#v(0.4cm)
#block[$d_8 = display(2 times 6.5 times 10^(-7) / 0.78005) approx 1.667$ мкм $= 1.667 times 10^(-6)$ м]

#v(0.5cm)

Среднее значение:

#align(center)[
  $overline(d) = display((1.679 + 1.667 + 1.662 + 1.667 + 1.665 + 1.668 + 1.667 + 1.667) / 8) approx 1.668$ мкм
]

#v(0.5cm)

Среднеквадратичное отклонение и погрешность среднего:

#align(center)[
  $sigma_d = sqrt(display(sum_(i=1)^(8) (d_i - overline(d))^2 / 7)) approx 0.005$ мкм, $quad sigma_(overline(d)) = display(sigma_d / sqrt(8)) approx 0.002$ мкм
]

#v(0.5cm)

Абсолютная погрешность (коэффициент Стьюдента для $n = 8$, $P = 0.95$: $t = 2.365$):

#align(center)[
  $Delta d = t dot sigma_(overline(d)) = 2.365 times 0.002 approx 0.004$ мкм
]

#v(0.5cm)

Относительная погрешность:

#align(center)[
  $epsilon = display(Delta d / overline(d)) = display(0.004 / 1.668) approx 0.24%$
]

#v(0.5cm)

*Вывод:*

#v(0.5cm)

Методом дифракции лазерного излучения ($lambda = 650$ нм) на голографической решётке определён её период. По 8 измерениям при $L$ от 0.15 до 0.30 м получено:

#align(center)[
  $d = (1.668 plus.minus 0.004)$ мкм $= (1.668 plus.minus 0.004) times 10^(-6)$ м
]

Относительная погрешность — 0.24%. Полученное значение соответствует решётке с плотностью штрихов ~599 мм#super[–1], что совпадает с номинальным значением 600 штр/мм.
