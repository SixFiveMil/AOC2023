import re

def main():
  z = 0
  f = open("input", "r")
  for x in f:
    temp = re.findall(r'\d', x)
    res = list(map(int, temp))
    if len(res) >= 1:
      z += int(str(res[0]) + str(res[-1]))
  print(z)

if __name__ == "__main__":
  main()
