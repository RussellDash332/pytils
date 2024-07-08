def solve(*exp):
    def check_back(exp, assgn, carry):
        try:
            d = carry
            for i in exp[:-1]:
                if i: d += assgn[i[-1]]
            e = assgn[exp[-1][-1]]
            return (d % 10 == e % 10, d//10)
        except: return False
    def backtrack(exp, domains, assgn, carry=0):
        for i in leads:
            if i in assgn and assgn[i] == 0: return
        if not any(exp) and carry == 0: return mem.add(tuple(sorted(assgn.items())))
        t = check_back(exp, assgn, carry)
        if not (type(t) == tuple and not t[0]):
            if t != False:
                exp = list(map(lambda x: x[:-1], exp)); carry = t[1]
                if not any(exp[:-1]) and exp[-1] and carry:
                    if exp[-1][-1] in assgn and assgn[exp[-1][-1]] == carry: return mem.add(tuple(sorted(assgn.items())))
                    if exp[-1][-1] not in assgn and carry in domains: return mem.add(tuple(sorted(list(assgn.items()) + [(exp[-1][-1], carry)])))
            if not any(exp) and not carry: return mem.add(tuple(sorted(assgn.items())))
            rec = False
            for i in {i[-1] for i in exp if i}:
                if i not in assgn:
                    rec = True
                    for domain in sorted(domains): assgn[i] = domain; domains -= {assgn[i]}; backtrack(exp, domains, assgn, carry); domains.add(assgn[i]); del assgn[i]
                    break
            if t != False and not rec: backtrack(exp, domains, assgn, carry)
    mem = set()
    domains = {*range(10)}
    leads = {i[0] for i in exp}
    letters = set()
    for i in exp: letters |= {*i}
    backtrack(exp, domains, {})
    # Output formatting
    print('-'*30)
    print(' + '.join(exp[:-1])+' = '+exp[-1])
    for asg in mem:
        asg = dict(asg)
        tmp = [*exp]
        for i in range(len(exp)):
            for j in {*exp[i]}: tmp[i] = tmp[i].replace(j, str(asg[j]))
        print(' + '.join(tmp[:-1])+' = '+tmp[-1])

solve('AB', 'AB', 'BCC')
solve('ARA', 'ABA', 'BAR')
solve('AIR', 'AR', 'IRA')
solve('SEND', 'MORE', 'MONEY')
solve('GREAT', 'SWERC', 'PORTO')            # multiple solutions
solve('TOO', 'GOOD', 'TO', 'BE', 'TRUE')    # >2 addendums
solve('ABCDE', 'ABCDE', 'ABCDE', 'ABCDE', 'EDCBA')
solve(                                      # longest cryptarithm by far
    'SO', 'MANY', 'MORE', 'MEN', 'SEEM',
    'TO', 'SAY', 'THAT', 'THEY', 'MAY',
    'SOON', 'TRY', 'TO', 'STAY', 'AT', 'HOME',
    'SO', 'AS', 'TO', 'SEE', 'OR', 'HEAR', 'THE',
    'SAME', 'ONE', 'MAN', 'TRY', 'TO', 'MEET', 'THE',
    'TEAM', 'ON', 'THE', 'MOON', 'AS', 'HE', 'HAS',
    'AT', 'THE', 'OTHER', 'TEN', 'TESTS'
)
