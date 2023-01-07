# def a1_func():
#     print("running a1_func()")
    
    
# # import other
# # import pack_a.a2
# # import pack_a.sub_a.sa1

# import sys
# for x in sys.path:
#     print(x)

# import other
# import a2
# from sub_a import sa1


# # print(a2.name)
# # print(sa1.name)

# # import other
# # from a2 import name
# # import sub_a.sa1


from pack_a.sub_a import sa2
import sys
for x in sys.path:
    print(x)
print(sa2.name)