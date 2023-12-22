deg, dis = map(int, input().split())
ans_deg = 'N'
w = 0
points = [
        (112.5, "N"),
        (337.5, "NNE"),
        (562.5, "NE"),
        (787.5, "ENE"),
        (1012.5, "E"),
        (1237.5, "ESE"),
        (1462.5, "SE"),
        (1687.5, "SSE"),
        (1912.5, "S"),
        (2137.5, "SSW"),
        (2362.5, "SW"),
        (2587.5, "WSW"),
        (2812.5, "W"),
        (3037.5, "WNW"),
        (3262.5, "NW"),
        (3487.5, "NNW"),
    ]
for th, d in points:
        if deg < th:
            ans_deg = d
            break


if dis < 15:
  w = 0
  ans_deg = 'C'
elif dis < 93:
  w = 1
elif dis < 201:
  w = 2
elif dis < 327:
  w = 3
elif dis < 477:
  w = 4
elif dis < 645:
  w = 5
elif dis < 831:
  w = 6
elif dis < 1029:
  w = 7
elif dis < 1245:
  w = 8
elif dis < 1467:
  w = 9
elif dis < 1707:
  w = 10
elif dis < 1959:
  w = 11
else:
  w = 12
print(ans_deg, w)

