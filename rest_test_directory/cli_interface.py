import requ

print('What u wanna do?\n Find pic by tag (1) \n Upload new untagged pic (2)')
desicion = input()
if desicion == '1':
    while True:
        print('Type tag to find image')
        tag = input()
        if requ.get_image(tag)[1]:
            print('Picture found!')
            break
        else:
            print('Please type again, tag not found!')

elif desicion == '2':
    print('Type link')
    link = input()
    requ.upload_untagged_image(link)
    print('Picture succesfully uploaded')


