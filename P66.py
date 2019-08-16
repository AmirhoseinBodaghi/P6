def main() :
    import os #for giving adress to where we want to save output files
    from openpyxl import load_workbook
    wb = load_workbook('OlympicAthletesData.xlsx')
    ws = wb.active
    Sport=[]
    Country=[]
    Name=[]
    Gender=[]
    ID=[]
    N_Post=[]
    N_Follower=[]
    N_Following=[]
    Max_Like=[]
    Max_Comment=[]
    Self_Presenting=[]
    Pure_Self_Presenting=[]

    #getting data of each column of excel file into a list named by the name of corrospondant name of that column 
    for row in ws :
        Sport.append(row[0].value)
        Country.append(row[1].value)
        Name.append(row[2].value)
        Gender.append(row[3].value)
        ID.append(row[4].value)
        N_Post.append(row[5].value)
        N_Follower.append(row[6].value)
        N_Following.append(row[7].value)
        Max_Like.append(row[8].value)
        Max_Comment.append(row[9].value)
        Self_Presenting.append(row[10].value)
        Pure_Self_Presenting.append(row[11].value)

    del Sport [0]
    del Country [0]
    del Name [0]
    del Gender [0]
    del ID [0]
    del N_Post [0]
    del N_Follower [0]
    del N_Following [0]
    del Max_Like [0]
    del Max_Comment [0]
    del Self_Presenting [0]
    del Pure_Self_Presenting [0]
    
    #------------------------------------
    #finding the number of users in dataset
    number_of_users_in_dataset = len (Name)
    pure_users = [] #users without their duplications (for example if a user has won more than one medal then the repititions would be omitted)
    pure_users_index = [] #pure users' index 
    pure_users_accessed_index = [] #pure users' index with their instagram account available 

    for n in Name:
        if n not in pure_users :
            pure_users.append (n)
            z = Name.index(n)
            pure_users_index.append(z)
            if ID[z]:
                pure_users_accessed_index.append(z)                

    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("number_of_users_in_dataset (number of individual gold medals) : ", number_of_users_in_dataset)
    print ("number_of_pure_users (number of champions who won the gold medals (one champion might have won more than one gold medal) : ", len(pure_users))
    print ("number_of_pure_users_with_insta_account_available  : ", len(pure_users_accessed_index))

    #------------------------------------        
    #finding the number of male and female users in dataset
    f_number = 0
    m_number = 0
    for i in pure_users_accessed_index : 
        if Gender[i] == "f" :
            f_number += 1
        elif Gender[i] == "m" :
            m_number += 1
        else :
            print("aha")

        
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("number_female_users : ", f_number)
    print ("number_male_users : ", m_number)
    
    #------------------------------------
    #finding the mean number of self presenting posts for male and female users in dataset
    i=0 
    Sum_Self_Presenting_Females = 0
    Sum_Pure_Self_Presenting_Females = 0
    Sum_Self_Presenting_Males = 0
    Sum_Pure_Self_Presenting_Males = 0
    for i in pure_users_accessed_index :
        if Gender[i] == "f" :
            t = Self_Presenting[i]
            tt = Pure_Self_Presenting[i]
            Sum_Self_Presenting_Females += int(t)
            Sum_Pure_Self_Presenting_Females += int(tt)
        elif Gender[i] == "m" :
            w = Self_Presenting[i]
            ww = Pure_Self_Presenting[i]
            Sum_Self_Presenting_Males += int(w)
            Sum_Pure_Self_Presenting_Males += int(ww)
        
        
    Mean_Self_Presenting_Females = Sum_Self_Presenting_Females/f_number
    Mean_Pure_Self_Presenting_Females = Sum_Pure_Self_Presenting_Females/f_number
    Mean_Self_Presenting_Males = Sum_Self_Presenting_Males/m_number
    Mean_Pure_Self_Presenting_Males = Sum_Pure_Self_Presenting_Males/m_number
    
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("number_female_users : ", f_number)
    print ("number_male_users : ", m_number)
    
    #-----------------------------------
    #finding the mean number of followers for male and female users in dataset
    sum_number_of_followers_for_all_females = 0
    sum_number_of_followers_for_all_males = 0
    for i in pure_users_accessed_index : 
        if Gender[i] == "f" :
            t = N_Follower[i]
            sum_number_of_followers_for_all_females += int(t)
        elif Gender[i] == "m" :
            w = N_Follower[i]
            sum_number_of_followers_for_all_males += int(w)

        
    mean_number_of_followers_for_females = sum_number_of_followers_for_all_females/f_number
    mean_number_of_followers_for_males = sum_number_of_followers_for_all_males/m_number

    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("mean_number_of_followers_for_females : ", mean_number_of_followers_for_females)
    print ("mean_number_of_followers_for_males : ", mean_number_of_followers_for_males)
    
    #-------------------------------------
    #finding the mean number of followings for male and female users in dataset
    sum_number_of_followings_for_all_females = 0
    sum_number_of_followings_for_all_males = 0
    for i in pure_users_accessed_index : 
        if Gender[i] == "f" :
            t = N_Following [i]
            sum_number_of_followings_for_all_females += int(t)
        elif Gender[i] == "m" :
            w = N_Following [i]
            sum_number_of_followings_for_all_males += int(w)

        
    mean_number_of_followings_for_females = sum_number_of_followings_for_all_females/f_number
    mean_number_of_followings_for_males = sum_number_of_followings_for_all_males/m_number

    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("mean_number_of_followings_for_females : ", mean_number_of_followings_for_females)
    print ("mean_number_of_followings_for_males : ", mean_number_of_followings_for_males)
    
    #-------------------------------------
    #finding the mean number of posts for male and female users in dataset
    sum_number_of_posts_for_all_females = 0
    sum_number_of_posts_for_all_males = 0
    for i in pure_users_accessed_index : 
        if Gender[i] == "f" :
            t = N_Post[i]
            sum_number_of_posts_for_all_females += int(t)
        elif Gender[i] == "m" :
            w = N_Post[i]
            sum_number_of_posts_for_all_males += int(w)
        
    mean_number_of_posts_for_females = sum_number_of_posts_for_all_females/f_number
    mean_number_of_posts_for_males = sum_number_of_posts_for_all_males/m_number

    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("mean_number_of_posts_for_females : ", mean_number_of_posts_for_females)
    print ("mean_number_of_posts_for_males : ", mean_number_of_posts_for_males)
    
    #-------------------------------------
    #finding the ratio of following/follower , like/following , like/follower , comment/following , comment/follower , self-presenting/10 , pure-self-presenting/10 , pure-self-presenting/self-presenting for all users
    ratio_of_followings_to_followers_for_all_users = []
    ratio_of_likes_to_followings_for_all_users = []
    ratio_of_likes_to_followers_for_all_users = []
    ratio_of_comment_to_followings_for_all_users = []
    ratio_of_comment_to_followers_for_all_users = []
    ratio_of_self_presenting_for_all_users = []
    ratio_of_pure_self_presenting_for_all_users = []
    ratio_of_pure_self_presenting_to_self_presenting_for_all_users = []
    
    for i in pure_users_accessed_index :
        t_1 = N_Following[i]/N_Follower[i]
        ratio_of_followings_to_followers_for_all_users.append(t_1)  #following/follower
        #----
        t_2 = Max_Like[i]/N_Following[i]
        ratio_of_likes_to_followings_for_all_users.append(t_2)  #like/following
        #----
        t_3 = Max_Like[i]/N_Follower[i]
        ratio_of_likes_to_followers_for_all_users.append(t_3)  #like/follower
        #----
        t_4 = Max_Comment[i]/N_Following[i]
        ratio_of_comment_to_followings_for_all_users.append(t_4)  #comment/following
        #----
        t_5 = Max_Comment[i]/N_Follower[i]
        ratio_of_comment_to_followers_for_all_users.append(t_5)  #comment/follower
        #----
        t_6 = Self_Presenting[i]/10
        ratio_of_self_presenting_for_all_users.append(t_6)  #self_presenting/10
        #----
        t_7 = Pure_Self_Presenting[i]/10
        ratio_of_pure_self_presenting_for_all_users.append(t_7)  #pure_self_presenting/10
        #----
        t_8 = Pure_Self_Presenting[i]/Self_Presenting[i]
        ratio_of_pure_self_presenting_to_self_presenting_for_all_users.append(t_8)  #pure_self_presenting/self_presenting
        
    #---------------------------------------------------------
    #-------- Hist2D : like/follower & following/follower
    #finding the relation between the ratio of "mean number of likes for posts(based on ex 10th 11th 12th posts)/follower" and the ratio of "following/follower"
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.colors as mcolors
    import matplotlib.mlab as mlab
    import os #To give address for saving output plots

##    print("MAX[ratio_of_like_to_follower_for_all_users] = " , max(ratio_of_likes_to_followers_for_all_users)) #we need this line to set max limit for horizental axis in plt.hist2d command (two lines below), which is 0.92 (we set to 1 ) , notice once we run the program and see the 0.92 then we set it in plt.hist2d for ever
##    print("MAX[ratio_of_followings_to_followers_for_all_users] = " , max(ratio_of_followings_to_followers_for_all_users)) #we need this line to set max limit for vertical axis in plt.hist2d command (two lines below), which is 15.66 (we set to 16 ) , notice once we run the program and see the 15.66 then we set it in plt.hist2d for ever
    plt.hist2d(ratio_of_likes_to_followers_for_all_users,ratio_of_followings_to_followers_for_all_users,8,[[0,0.5],[0,0.5]])
    plt.xlabel('Like/Follower ratio')
    plt.ylabel('Following/Follower ratio')
    ##    plt.title('Like/Follower & Following/Follower',fontsize=12)
    file_name = "Hist2D_LikeFollower_to_FollowingFollower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
    cbar = plt.colorbar() #the reason why we don't use only plt.colorbar() lonely , is that we want to put a label close it, so we used this line and next line 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
    ##    plt.show()
    #---- Hist2D : like/follower & following/follower --- its the above hist2d but here we just focus on the dense area  
    plt.hist2d(ratio_of_likes_to_followers_for_all_users,ratio_of_followings_to_followers_for_all_users,12,[[0,0.5],[0,0.5]])
    plt.xlabel('Like/Follower ratio')
    plt.ylabel('Following/Follower ratio')
    ##    plt.title('Like/Follower & Following/Follower (focused)',fontsize=12)
    file_name = "Hist2Dfocused_LikeFollower_to_FollowingFollower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
    cbar = plt.colorbar() #the reason why we don't use only plt.colorbar() lonely , is that we want to put a label close it, so we used this line and next line 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
    ##    plt.show()
    #---- Hist2D : pure-self-presenting/self-presenting & following/follower  
    plt.hist2d(ratio_of_pure_self_presenting_to_self_presenting_for_all_users,ratio_of_followings_to_followers_for_all_users,12,[[0,1],[0,0.5]])
    plt.xlabel('pure_self_presenting/self_presenting ratio')
    plt.ylabel('Following/Follower ratio')
    ##    plt.title('Like/Follower & Following/Follower (focused)',fontsize=12)
    file_name = "Hist2D_pureSF-SF_to_FollowingFollower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
    cbar = plt.colorbar() #the reason why we don't use only plt.colorbar() lonely , is that we want to put a label close it, so we used this line and next line 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
    ##    plt.show()
    #---- Hist2D : pure-self-presenting/self-presenting & like/follower  
    plt.hist2d(ratio_of_pure_self_presenting_to_self_presenting_for_all_users,ratio_of_likes_to_followers_for_all_users,12,[[0,1],[0,1]])
    plt.xlabel('pure_self_presenting/self_presenting ratio')
    plt.ylabel('Like/Follower ratio')
    ##    plt.title('Like/Follower & Following/Follower (focused)',fontsize=12)
    file_name = "Hist2D_pureSF-SF_to_LikeFollower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
    cbar = plt.colorbar() #the reason why we don't use only plt.colorbar() lonely , is that we want to put a label close it, so we used this line and next line 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
    #-------- Hist1D : following/follower 
    plt.hist(ratio_of_followings_to_followers_for_all_users,[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16]) #we set the edges of bins for histogram from 0 to 16(which is the max in the dataset and we noticed that from previous command  
    #--------     
    plt.xlabel('Following/Follower ratio')
    plt.ylabel('Frequency')
    ##    plt.title('Like/Follower',fontsize=12)
    file_name = "Hist1D_Following_to_Follower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
    #-------- Hist1D : like/follower
    plt.hist(ratio_of_likes_to_followers_for_all_users,[0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]) #we set the edges of bins for histogram from 0 to 0.92(which is the max in the dataset and we noticed that from previous commands  
    #--------     
    plt.xlabel('Like/Follower ratio')
    plt.ylabel('Frequency')
    ##    plt.title('Like/Follower',fontsize=12)
    file_name = "Hist1D_Like_to_Follower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
    ##    plt.show()
    #-------- 

    #-----------------------------------------------------------
    #great result :
    #THOSE USERS WITH FOLLOWEING/FOLLOWER < 1 WITH STRONGER PROBABILITY HAVE BETTER CHANCE OF ACCEPTANCE . In other words they have better like/follower (like/following) , so the chance that they start the rumor are more stronger 
    #-----------------------------------------------------------    
    #PLEASE notice that if we use discrete values of 0,1,2,3,..,9,10 as number of self posts(narcissism) then hist2d shape would be discrete that is not good, so for each number we randomly choose a value between two defined limit. for example if self posts number is 2 then we choose ranmoly a number between (0.2 , 0.3) to represent its narcissism level
    import matplotlib.pyplot as plt
    import numpy
    import random
    narcissism = [] #all self presenting posts    
    for i in pure_users_accessed_index :
        if Self_Presenting[i] == 0 :
            t = random.uniform(0,0.01)
            narcissism.append (t)
        elif Self_Presenting[i] == 1 :
            t = random.uniform(0.01,0.1)
            narcissism.append (t)
        elif Self_Presenting[i] == 2 :
            t = random.uniform(0.1,0.2)
            narcissism.append (t)
        elif Self_Presenting[i] == 3 :
            t = random.uniform(0.2,0.3)
            narcissism.append (t)
        elif Self_Presenting[i] == 4 :
            t = random.uniform(0.3,0.4)
            narcissism.append (t)
        elif Self_Presenting[i] == 5 :
            t = random.uniform(0.4,0.5)
            narcissism.append (t)
        elif Self_Presenting[i] == 6 :
            t = random.uniform(0.5,0.6)
            narcissism.append (t)
        elif Self_Presenting[i] == 7 :
            t = random.uniform(0.6,0.7)
            narcissism.append (t)
        elif Self_Presenting[i] == 8 :
            t = random.uniform(0.7,0.8)
            narcissism.append (t)
        elif Self_Presenting[i] == 9 :
            t = random.uniform(0.8,0.9)
            narcissism.append (t)
        elif Self_Presenting[i] == 10 :
            t = random.uniform(0.9,1)
            narcissism.append (t)
            
#---- #Finding the relation between the number of self posts(in 10 previous posts) (NARCISSISM) and the ratio of like/follower
    plt.hist2d(narcissism,ratio_of_likes_to_followers_for_all_users,12,[[0,1],[0,0.5]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Like/Follower')
##    plt.title('narcissism & Like/Follower ratio',fontsize=12)
    file_name = "Hist2D_narcissism_to_LikeFollower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
    cbar = plt.colorbar() #the reason why we don't use only plt.colorbar() lonely , is that we want to put a label close it, so we used this line and next line 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
##    plt.show()
#---- #finding the relation between NARCISSISM and the ratio of following/follower"
    plt.hist2d(narcissism,ratio_of_followings_to_followers_for_all_users,12,[[0,1],[0,1]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Following/Follower')
##    plt.title('narcissism & Following/Follower ratio',fontsize=12)
    file_name = "Hist2D_narcissism_to_FollowingFollower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
    cbar = plt.colorbar() #the reason why we don't use only plt.colorbar() lonely , is that we want to put a label close it, so we used this line and next line 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
    ##    plt.show()
##----------
    narcissism_pure = [] #all pure self presenting posts
    for i in pure_users_accessed_index :
        if Pure_Self_Presenting[i] == 0 :
            tt = random.uniform(0,0.01)
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 1 :
            tt = random.uniform(0.01,0.1)
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 2 :
            tt = random.uniform(0.1,0.2)
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 3 :
            tt = random.uniform(0.2,0.3)
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 4 :
            tt = random.uniform(0.3,0.4)
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 5 :
            tt = random.uniform(0.4,0.5)
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 6 :
            tt = random.uniform(0.5,0.6)
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 7 :
            tt = random.uniform(0.6,0.7)
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 8 :
            tt = random.uniform(0.7,0.8)
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 9 :
            tt = random.uniform(0.8,0.9)
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 10 :
            tt = random.uniform(0.9,1)
            narcissism_pure.append (tt)

#---- #Finding the relation between Pure-NARCISSISM and the ratio of like/follower            
    plt.hist2d(narcissism_pure,ratio_of_likes_to_followers_for_all_users,6,[[0,1],[0,1]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Like/Follower')
##    plt.title('narcissism & Like/Follower ratio',fontsize=12)
    file_name = "Hist2D_pure_narcissism_to_LikeFollower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
    cbar = plt.colorbar() #the reason why we don't use only plt.colorbar() lonely , is that we want to put a label close it, so we used this line and next line 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
##    plt.show()
#---- #finding the relation between Pure-NARCISSISM and the ratio of following/follower"
    plt.hist2d(narcissism_pure,ratio_of_followings_to_followers_for_all_users,12,[[0,1],[0,1]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Following/Follower')
##    plt.title('narcissism & Following/Follower ratio',fontsize=12)
    file_name = "Hist2D_pure_narcissism_to_FollowingFollower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
    cbar = plt.colorbar() #the reason why we don't use only plt.colorbar() lonely , is that we want to put a label close it, so we used this line and next line 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
    ##    plt.show()


##    return name,number_of_posts,number_of_followers,number_of_followings,mean_like_for_all_users,number_of_self_picture_posts_form_9_previous_posts,sex,narcissism,ratio_of_followings_to_followers_for_all_users,mean_like_to_follower_for_all_users,cc , cx , cxx , cxxx, cy , cyy , cyyy , cq




                                #          Compare      Main_dataset_after_150_days       with         Main_dataset             #

    import numpy
    from scipy.stats import pearsonr
    from scipy.stats import spearmanr


    # pearson correlation 
    fwtofr_to_litofr = pearsonr(ratio_of_followings_to_followers_for_all_users,ratio_of_likes_to_followers_for_all_users)
    fwtofr_to_cmtofr = pearsonr(ratio_of_followings_to_followers_for_all_users,ratio_of_comment_to_followers_for_all_users)
    fwtofr_to_narcissism = pearsonr(ratio_of_followings_to_followers_for_all_users,ratio_of_self_presenting_for_all_users)
    fwtofr_to_pure_narcissism = pearsonr(ratio_of_followings_to_followers_for_all_users,ratio_of_pure_self_presenting_for_all_users)
    fwtofr_to_npn = pearsonr(ratio_of_followings_to_followers_for_all_users,ratio_of_pure_self_presenting_to_self_presenting_for_all_users)

    litofr_to_narcissism = pearsonr(ratio_of_likes_to_followers_for_all_users,ratio_of_self_presenting_for_all_users)
    litofr_to_pure_narcissism = pearsonr(ratio_of_likes_to_followers_for_all_users,ratio_of_pure_self_presenting_for_all_users)
    litofr_to_npn = pearsonr(ratio_of_likes_to_followers_for_all_users,ratio_of_pure_self_presenting_to_self_presenting_for_all_users)

    # spearman correlation 
    fwtofr_to_litofr = spearmanr(ratio_of_followings_to_followers_for_all_users,ratio_of_likes_to_followers_for_all_users)
    fwtofr_to_cmtofr = spearmanr(ratio_of_followings_to_followers_for_all_users,ratio_of_comment_to_followers_for_all_users)
    fwtofr_to_narcissism = spearmanr(ratio_of_followings_to_followers_for_all_users,ratio_of_self_presenting_for_all_users)
    fwtofr_to_pure_narcissism = spearmanr(ratio_of_followings_to_followers_for_all_users,ratio_of_pure_self_presenting_for_all_users)
    fwtofr_to_npn = spearmanr(ratio_of_followings_to_followers_for_all_users,ratio_of_pure_self_presenting_to_self_presenting_for_all_users)

    litofr_to_narcissism = spearmanr(ratio_of_likes_to_followers_for_all_users,ratio_of_self_presenting_for_all_users)
    litofr_to_pure_narcissism = spearmanr(ratio_of_likes_to_followers_for_all_users,ratio_of_pure_self_presenting_for_all_users)
    litofr_to_npn = spearmanr(ratio_of_likes_to_followers_for_all_users,ratio_of_pure_self_presenting_to_self_presenting_for_all_users)




    print (" --------------------------------------------- Statistics of both Datasets  ----------------------------------------- ")
    print (" ------------------------------------------------ Pearson --------------------------------------------- ")
    print (" fwtofr_to_litofr : ", fwtofr_to_litofr)
    print (" fwtofr_to_cmtofr : ", fwtofr_to_cmtofr)
    print (" fwtofr_to_narcissism : ", fwtofr_to_narcissism)
    print (" fwtofr_to_pure_narcissism : ", fwtofr_to_pure_narcissism)
    print (" fwtofr_to_npn : ", fwtofr_to_npn)
    print (" litofr_to_narcissism : ", litofr_to_narcissism)
    print (" litofr_to_pure_narcissism : ", litofr_to_pure_narcissism)
    print (" litofr_to_npn : ", litofr_to_npn)
    print (" --------------------------------------------------------------------------------------------------------------------- ")
    print (" ------------------------------------ Spearman ------------------------------------ ")
    print (" fwtofr_to_litofr : ", fwtofr_to_litofr)
    print (" fwtofr_to_cmtofr : ", fwtofr_to_cmtofr)
    print (" fwtofr_to_narcissism : ", fwtofr_to_narcissism)
    print (" fwtofr_to_pure_narcissism : ", fwtofr_to_pure_narcissism)
    print (" fwtofr_to_npn : ", fwtofr_to_npn)
    print (" litofr_to_narcissism : ", litofr_to_narcissism)
    print (" litofr_to_pure_narcissism : ", litofr_to_pure_narcissism)
    print (" litofr_to_npn : ", litofr_to_npn)

#--------------------
main()
input("\n press enter key to exit.")
