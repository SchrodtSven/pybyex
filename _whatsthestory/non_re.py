source='your token _here0@df and maybe _here1@df or maybe _here2@df'
start_sep='_'
end_sep='@df'
result=[]
tmp=source.split(start_sep)
for par in tmp:
  if end_sep in par:
    result.append(par.split(end_sep)[0])

print(result)