def fun(s):
    if s.count('@') > 1 or s.count('.') > 1:
        return False
    if '@' in s:
        user, x = s.split('@')
    else:
        return False

    if '.' in x:
        site, ext = x.split('.')
    else:
        return False

    user = user.replace('-', '')
    user = user.replace('_', '')

    if not user.isalnum():
        return False
    elif not site.isalnum():
        return False
    elif len(ext) > 3:
        return False
    else:
        return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)