def radix_sort(accounts):
    
    max_length = max(len(account) for account in accounts)
    
    # iteramos do dígito mais a direita para o mais a equerda
    for position in range(max_length - 1, -1, -1):
        # buckets para cada dígito da conta
        buckets = [[] for _ in range(16)]
        for account in accounts:
            index = position if position < len(account) else 0
            char = account[index]
            # converte dígito para inteiro
            if char.isdigit():
                bucket_index = int(char)
            else:
                bucket_index = ord(char) - ord('A') + 10
            # inserimos a conta no bucket referente ao dígito atual sobre o qual iteramos
            buckets[bucket_index].append(account)
        # Combinar os buckets de volta na lista accounts
        accounts = [account for bucket in buckets for account in bucket]
    # Aproveitamos a estabilidade do algoritmo sempre que fazemos uma inserção no bucket para garantir a ordenação no final
    return accounts

def process_accounts(raw_accounts):
    # removendo espaços e contando operações da conta
    account_frequency = {}
    for raw_account in raw_accounts:
        account = raw_account.replace(" ", "")
        if account in account_frequency:
            account_frequency[account] += 1
        else:
            account_frequency[account] = 1

    # criamos uma lista onde as contas só aparecem uma vez e a ordenamos
    unique_accounts = list(account_frequency.keys())
    sorted_accounts = radix_sort(unique_accounts)
    
    print(len(sorted_accounts))
    for account in sorted_accounts:
        # conversao das contas para o formato da entrada
        formatted_account = f"{account[:2]} {account[2:10]} {account[10:14]} {account[14:18]} {account[18:22]} {account[22:]}"
        print(f"{formatted_account} {account_frequency[account]}")


n = int(input())
raw_accounts = []
# Lemos as n contas e as guardamos (na formatacao original)
for i in range(n):
    current_account = input()
    raw_accounts.append(current_account)

process_accounts(raw_accounts)
