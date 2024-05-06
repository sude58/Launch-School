info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

infos = info.split(':')
info_2 = '+'.join(infos)
print(info_2)

# Alternative in documentation
info_3 = info.replace(':', '+')
print(info_3)