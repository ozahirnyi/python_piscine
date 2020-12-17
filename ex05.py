t = (19, 42, 21)
print("The 3 numbers are: %d, %d, %d" % t)

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}
for key, value in languages.items():
    print("%s was created by %s" % (key, value))

q = (3, 30, 2019, 9, 25)
print("0%d/%d/%d 0%d:%d" % (q[3], q[4], q[2], q[0], q[1]))

kata03 = "The right format"
res = kata03.rjust(42, '-')
print(res)
