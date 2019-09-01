def main() :
    import os #for giving adress to where we want to save output files
    from openpyxl import load_workbook
    import random
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
    Age=[]

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
        Age.append(row[12].value)

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
    del Age [0]
    
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
    ratio_of_followings_to_followers_f  = []
    ratio_of_likes_to_followings_f = []
    ratio_of_likes_to_followers_f = []
    ratio_of_comment_to_followings_f = []
    ratio_of_comment_to_followers_f = []
    ratio_of_self_presenting_f = []
    ratio_of_pure_self_presenting_f = []
    ratio_of_pure_self_presenting_to_self_presenting_f = []
    ratio_of_engagement_to_followers_f = []
    age_pure_f = []
    narcissism_f = []
    narcissism_pure_f = []

    m_number = 0
    ratio_of_followings_to_followers_m  = []
    ratio_of_likes_to_followings_m = []
    ratio_of_likes_to_followers_m = []
    ratio_of_comment_to_followings_m = []
    ratio_of_comment_to_followers_m = []
    ratio_of_self_presenting_m = []
    ratio_of_pure_self_presenting_m = []
    ratio_of_pure_self_presenting_to_self_presenting_m = []
    ratio_of_engagement_to_followers_m = []
    age_pure_m = []
    narcissism_m = []
    narcissism_pure_m = []
    
    for i in pure_users_accessed_index : 
        if Gender[i] == "f" :
            f_number += 1
            t_1_f = N_Following[i]/N_Follower[i]
            ratio_of_followings_to_followers_f.append(t_1_f)
            t_2_f = Max_Like[i]/N_Following[i]
            ratio_of_likes_to_followings_f.append(t_2_f)
            t_3_f = Max_Like[i]/N_Follower[i]
            ratio_of_likes_to_followers_f.append(t_3_f)
            t_4_f = Max_Comment[i]/N_Following[i]
            ratio_of_comment_to_followings_f.append(t_4_f)
            t_5_f = Max_Comment[i]/N_Follower[i]
            ratio_of_comment_to_followers_f.append(t_5_f)
            t_6_f = Self_Presenting[i]/10
            ratio_of_self_presenting_f.append(t_6_f)
            t_7_f = Pure_Self_Presenting[i]/10
            ratio_of_pure_self_presenting_f.append(t_7_f)
            t_8_f = Pure_Self_Presenting[i]/Self_Presenting[i]
            ratio_of_pure_self_presenting_to_self_presenting_f.append(t_8_f)
            engagement = Max_Like[i] + Max_Comment[i]
            t_9_f = engagement/N_Follower[i]
            ratio_of_engagement_to_followers_f.append(t_9_f)
            t_10_f = Age [i]
            age_pure_f.append (t_10_f)
                
            if Self_Presenting[i] == 0 :
                t = 0.0001
                narcissism_f.append (t)
            elif Self_Presenting[i] == 1 :
                t = 0.1
                narcissism_f.append (t)
            elif Self_Presenting[i] == 2 :
                t = 0.2
                narcissism_f.append (t)
            elif Self_Presenting[i] == 3 :
                t = 0.3
                narcissism_f.append (t)
            elif Self_Presenting[i] == 4 :
                t = 0.4
                narcissism_f.append (t)
            elif Self_Presenting[i] == 5 :
                t = 0.5
                narcissism_f.append (t)
            elif Self_Presenting[i] == 6 :
                t = 0.6
                narcissism_f.append (t)
            elif Self_Presenting[i] == 7 :
                t = 0.7
                narcissism_f.append (t)
            elif Self_Presenting[i] == 8 :
                t = 0.8
                narcissism_f.append (t)
            elif Self_Presenting[i] == 9 :
                t = 0.9
                narcissism_f.append (t)
            elif Self_Presenting[i] == 10 :
                t = 1
                narcissism_f.append (t)

            if Pure_Self_Presenting[i] == 0 :
                tt = 0.0001
                narcissism_pure_f.append (tt)
            elif Pure_Self_Presenting[i] == 1 :
                tt = 0.1
                narcissism_pure_f.append (tt)
            elif Pure_Self_Presenting[i] == 2 :
                tt = 0.2
                narcissism_pure_f.append (tt)
            elif Pure_Self_Presenting[i] == 3 :
                tt = 0.3
                narcissism_pure_f.append (tt)
            elif Pure_Self_Presenting[i] == 4 :
                tt = 0.4
                narcissism_pure_f.append (tt)
            elif Pure_Self_Presenting[i] == 5 :
                tt = 0.5
                narcissism_pure_f.append (tt)
            elif Pure_Self_Presenting[i] == 6 :
                tt = 0.6
                narcissism_pure_f.append (tt)
            elif Pure_Self_Presenting[i] == 7 :
                tt = 0.7
                narcissism_pure_f.append (tt)
            elif Pure_Self_Presenting[i] == 8 :
                tt = 0.8
                narcissism_pure_f.append (tt)
            elif Pure_Self_Presenting[i] == 9 :
                tt = 0.9
                narcissism_pure_f.append (tt)
            elif Pure_Self_Presenting[i] == 10 :
                tt = 1
                narcissism_pure_f.append (tt)
            
        elif Gender[i] == "m" :
            m_number += 1
            t_1_m = N_Following[i]/N_Follower[i]
            ratio_of_followings_to_followers_m.append(t_1_m)
            t_2_m = Max_Like[i]/N_Following[i]
            ratio_of_likes_to_followings_m.append(t_2_m)
            t_3_m = Max_Like[i]/N_Follower[i]
            ratio_of_likes_to_followers_m.append(t_3_m)
            t_4_m = Max_Comment[i]/N_Following[i]
            ratio_of_comment_to_followings_m.append(t_4_m)
            t_5_m = Max_Comment[i]/N_Follower[i]
            ratio_of_comment_to_followers_m.append(t_5_m)
            t_6_m = Self_Presenting[i]/10
            ratio_of_self_presenting_m.append(t_6_m)
            t_7_m = Pure_Self_Presenting[i]/10
            ratio_of_pure_self_presenting_m.append(t_7_m)
            t_8_m = Pure_Self_Presenting[i]/Self_Presenting[i]
            ratio_of_pure_self_presenting_to_self_presenting_m.append(t_8_m)
            engagement = Max_Like[i] + Max_Comment[i]
            t_9_m = engagement/N_Follower[i]
            ratio_of_engagement_to_followers_m.append(t_9_m)
            t_10_m = Age [i]
            age_pure_m.append (t_10_m)

            if Self_Presenting[i] == 0 :
                t = 0.0001
                narcissism_m.append (t)
            elif Self_Presenting[i] == 1 :
                t = 0.1
                narcissism_m.append (t)
            elif Self_Presenting[i] == 2 :
                t = 0.2
                narcissism_m.append (t)
            elif Self_Presenting[i] == 3 :
                t = 0.3
                narcissism_m.append (t)
            elif Self_Presenting[i] == 4 :
                t = 0.4
                narcissism_m.append (t)
            elif Self_Presenting[i] == 5 :
                t = 0.5
                narcissism_m.append (t)
            elif Self_Presenting[i] == 6 :
                t = 0.6
                narcissism_m.append (t)
            elif Self_Presenting[i] == 7 :
                t = 0.7
                narcissism_m.append (t)
            elif Self_Presenting[i] == 8 :
                t = 0.8
                narcissism_m.append (t)
            elif Self_Presenting[i] == 9 :
                t = 0.9
                narcissism_m.append (t)
            elif Self_Presenting[i] == 10 :
                t = 1
                narcissism_m.append (t)

            if Pure_Self_Presenting[i] == 0 :
                tt = 0.0001
                narcissism_pure_m.append (tt)
            elif Pure_Self_Presenting[i] == 1 :
                tt = 0.1
                narcissism_pure_m.append (tt)
            elif Pure_Self_Presenting[i] == 2 :
                tt = 0.2
                narcissism_pure_m.append (tt)
            elif Pure_Self_Presenting[i] == 3 :
                tt = 0.3
                narcissism_pure_m.append (tt)
            elif Pure_Self_Presenting[i] == 4 :
                tt = 0.4
                narcissism_pure_m.append (tt)
            elif Pure_Self_Presenting[i] == 5 :
                tt = 0.5
                narcissism_pure_m.append (tt)
            elif Pure_Self_Presenting[i] == 6 :
                tt = 0.6
                narcissism_pure_m.append (tt)
            elif Pure_Self_Presenting[i] == 7 :
                tt = 0.7
                narcissism_pure_m.append (tt)
            elif Pure_Self_Presenting[i] == 8 :
                tt = 0.8
                narcissism_pure_m.append (tt)
            elif Pure_Self_Presenting[i] == 9 :
                tt = 0.9
                narcissism_pure_m.append (tt)
            elif Pure_Self_Presenting[i] == 10 :
                tt = 1
                narcissism_pure_m.append (tt)
            
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
    age_pure = []
    for i in pure_users_accessed_index :
        cc = Age[i]
        age_pure.append(cc)
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
    ratio_of_followings_to_followers = []
    ratio_of_likes_to_followings = []
    ratio_of_likes_to_followers = []
    ratio_of_comment_to_followings = []
    ratio_of_comment_to_followers = []
    ratio_of_self_presenting = []
    ratio_of_pure_self_presenting = []
    ratio_of_pure_self_presenting_to_self_presenting = []
    ratio_of_engagement_to_followers = []
    
    for i in pure_users_accessed_index :
        t_1 = N_Following[i]/N_Follower[i]
        ratio_of_followings_to_followers.append(t_1)  #following/follower
        #----
        t_2 = Max_Like[i]/N_Following[i]
        ratio_of_likes_to_followings.append(t_2)  #like/following
        #----
        t_3 = Max_Like[i]/N_Follower[i]
        ratio_of_likes_to_followers.append(t_3)  #like/follower
        #----
        t_4 = Max_Comment[i]/N_Following[i]
        ratio_of_comment_to_followings.append(t_4)  #comment/following
        #----
        t_5 = Max_Comment[i]/N_Follower[i]
        ratio_of_comment_to_followers.append(t_5)  #comment/follower
        #----
        t_6 = Self_Presenting[i]/10
        ratio_of_self_presenting.append(t_6)  #self_presenting/10
        #----
        t_7 = Pure_Self_Presenting[i]/10
        ratio_of_pure_self_presenting.append(t_7)  #pure_self_presenting/10
        #----
        t_8 = Pure_Self_Presenting[i]/Self_Presenting[i]
        ratio_of_pure_self_presenting_to_self_presenting.append(t_8)  #pure_self_presenting/self_presenting
        #----
        engagement = Max_Like[i] + Max_Comment[i]
        t_9 = engagement/N_Follower[i]
        ratio_of_engagement_to_followers.append(t_9)  #engagement/follower
        
        
    #---------------------------------------------------------
    #-------- Histogram of Results ---------------------------
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.colors as mcolors
    import matplotlib.mlab as mlab
    import os #To give address for saving output plots

##    #---- Hist2D : like/follower & following/follower
##    plt.hist2d(ratio_of_likes_to_followers,ratio_of_followings_to_followers,5,[[0,0.5],[0,0.5]])
##    plt.xlabel('Like/Follower ratio')
##    plt.ylabel('Following/Follower ratio')
##    file_name = "Hist2D_LikeFollower_to_FollowingFollower.tif"  # notice that if you set name as following/follower , I mean if you put / symbol in the name then it won't be saved! because symboles such this "/" must not be in file names
##    path_of_saving = str ("D:\\Papers\\Paper_6") #here we make the address of the folder we want pictures to be saved, BUT YOU HAVE TO douplicate each Backslash in the URL address (as you see I did ) , if you dont it wont work and give you error of UNICODESCAPE !
##    cbar = plt.colorbar() #the reason why we don't use only plt.colorbar() lonely , is that we want to put a label close it, so we used this line and next line 
##    cbar.set_label ("Frequency")
##    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
##    plt.close() 
##    #---- Hist2D : like/follower & following/follower --- its the above hist2d but here we just focus on the dense area  
##    plt.hist2d(ratio_of_likes_to_followers,ratio_of_followings_to_followers,5,[[0,0.5],[0,0.2]])
##    plt.xlabel('Like/Follower ratio')
##    plt.ylabel('Following/Follower ratio')
##    file_name = "Hist2Dfocused_LikeFollower_to_FollowingFollower.tif"  
##    path_of_saving = str ("D:\\Papers\\Paper_6")
##    cbar = plt.colorbar()  
##    cbar.set_label ("Frequency")
##    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
##    plt.close() 
    #---- Hist2D : pure-self-presenting/self-presenting & following/follower  
    plt.hist2d(ratio_of_pure_self_presenting_to_self_presenting,ratio_of_followings_to_followers,5,[[0,1],[0,0.5]])
    plt.xlabel('pure_self_presenting/self_presenting ratio')
    plt.ylabel('Following/Follower ratio')
    file_name = "Hist2D_pureSF-SF_to_FollowingFollower.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
##    #---- Hist2D : pure-self-presenting/self-presenting & like/follower  
##    plt.hist2d(ratio_of_pure_self_presenting_to_self_presenting,ratio_of_likes_to_followers,5,[[0,1],[0,1]])
##    plt.xlabel('pure_self_presenting/self_presenting ratio')
##    plt.ylabel('Like/Follower ratio')
##    file_name = "Hist2D_pureSF-SF_to_LikeFollower.tif" 
##    path_of_saving = str ("D:\\Papers\\Paper_6") 
##    cbar = plt.colorbar() 
##    cbar.set_label ("Frequency")
##    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
##    plt.close() 
    #-------- Hist1D : following/follower 
    plt.hist(ratio_of_followings_to_followers,[0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]) #we set the edges of bins for histogram from 0 to 1  
    #--------     
    plt.xlabel('Following/Follower ratio')
    plt.ylabel('Frequency')
    file_name = "Hist1D_Following_to_Follower.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
    #-------- Hist1D : like/follower
    plt.hist(ratio_of_likes_to_followers,[0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1])   
    #--------     
    plt.xlabel('Like/Follower ratio')
    plt.ylabel('Frequency')
    file_name = "Hist1D_Like_to_Follower.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6")  
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
    #PLEASE notice that if we use discrete values of 0,1,2,3,..,9,10 as number of self posts(narcissism) then hist2d shape would be discrete that is not good, so for each number we randomly choose a value between two defined limit. for example if self posts number is 2 then we choose ranmoly a number between (0.2 , 0.3) to represent its narcissism level
    import matplotlib.pyplot as plt
    import numpy
    import random
    narcissism = [] #all self presenting posts    
    for i in pure_users_accessed_index :
        if Self_Presenting[i] == 0 :
            t = 0.0001
            narcissism.append (t)
        elif Self_Presenting[i] == 1 :
            t = 0.1
            narcissism.append (t)
        elif Self_Presenting[i] == 2 :
            t = 0.2
            narcissism.append (t)
        elif Self_Presenting[i] == 3 :
            t = 0.3
            narcissism.append (t)
        elif Self_Presenting[i] == 4 :
            t = 0.4
            narcissism.append (t)
        elif Self_Presenting[i] == 5 :
            t = 0.5
            narcissism.append (t)
        elif Self_Presenting[i] == 6 :
            t = 0.6
            narcissism.append (t)
        elif Self_Presenting[i] == 7 :
            t = 0.7
            narcissism.append (t)
        elif Self_Presenting[i] == 8 :
            t = 0.8
            narcissism.append (t)
        elif Self_Presenting[i] == 9 :
            t = 0.9
            narcissism.append (t)
        elif Self_Presenting[i] == 10 :
            t = 1
            narcissism.append (t)
            
###---- #Finding the relation between the number of self posts(in 10 previous posts) (NARCISSISM) and the ratio of like/follower
##    plt.hist2d(narcissism,ratio_of_likes_to_followers,5,[[0,1],[0,0.5]])
##    plt.xlabel('Ratio of self-presenting posts')
##    plt.ylabel('Like/Follower')
##    file_name = "Hist2D_narcissism_to_LikeFollower.tif"  
##    path_of_saving = str ("D:\\Papers\\Paper_6") 
##    cbar = plt.colorbar()  
##    cbar.set_label ("Frequency")
##    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
##    plt.close() 
#---- #Finding the relation between NARCISSISM and the ratio of following/follower"
    plt.hist2d(narcissism,ratio_of_followings_to_followers,5,[[0,1],[0,1]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Following/Follower')
    file_name = "Hist2D_narcissism_to_FollowingFollower.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
##----------
    narcissism_pure = [] #all pure self presenting posts
    for i in pure_users_accessed_index :
        if Pure_Self_Presenting[i] == 0 :
            tt = 0.0001
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 1 :
            tt = 0.1
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 2 :
            tt = 0.2
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 3 :
            tt = 0.3
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 4 :
            tt = 0.4
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 5 :
            tt = 0.5
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 6 :
            tt = 0.6
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 7 :
            tt = 0.7
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 8 :
            tt = 0.8
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 9 :
            tt = 0.9
            narcissism_pure.append (tt)
        elif Pure_Self_Presenting[i] == 10 :
            tt = 1
            narcissism_pure.append (tt)

###---- #Finding the relation between Pure-NARCISSISM and the ratio of like/follower            
##    plt.hist2d(narcissism_pure,ratio_of_likes_to_followers,5,[[0,1],[0,1]])
##    plt.xlabel('Ratio of pure self-presenting posts')
##    plt.ylabel('Like/Follower')
##    file_name = "Hist2D_pure_narcissism_to_LikeFollower.tif"  
##    path_of_saving = str ("D:\\Papers\\Paper_6") 
##    cbar = plt.colorbar()  
##    cbar.set_label ("Frequency")
##    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
##    plt.close() 
#---- #finding the relation between Pure-NARCISSISM and the ratio of following/follower"
    plt.hist2d(narcissism_pure,ratio_of_followings_to_followers,5,[[0,1],[0,1]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Following/Follower')
    file_name = "Hist2D_pure_narcissism_to_FollowingFollower.tif" 
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between Pure-NARCISSISM and engagement/followers            
    plt.hist2d(narcissism_pure,ratio_of_engagement_to_followers,5,[[0,1],[0,1]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Engagement/Followers')
    file_name = "Hist2D_pure_narcissism_to_EngagementFollower.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between the number of self posts(in 10 previous posts) (NARCISSISM) and engagement/followers
    plt.hist2d(narcissism,ratio_of_engagement_to_followers,5,[[0,1],[0,0.5]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Engagement/Followers')
    file_name = "Hist2D_narcissism_to_EngagementFollower.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
#---- Hist2D : pure-self-presenting/self-presenting & engagement/followers  
    plt.hist2d(ratio_of_pure_self_presenting_to_self_presenting,ratio_of_engagement_to_followers,5,[[0,1],[0,1]])
    plt.xlabel('pure_self_presenting/self_presenting ratio')
    plt.ylabel('Engagement/Followers ratio')
    file_name = "Hist2D_pureSF-SF_to_EngagementFollower.tif" 
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- Hist2D : engagement/followers & following/follower
    plt.hist2d(ratio_of_engagement_to_followers,ratio_of_followings_to_followers,5,[[0,0.5],[0,0.5]])
    plt.xlabel('Engagement/Followers ratio')
    plt.ylabel('Following/Follower ratio')
    file_name = "Hist2D_EngagementFollower_to_FollowingFollower.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- Hist2D : engagement/followers & age
    plt.hist2d(ratio_of_engagement_to_followers,age_pure,5,[[0,0.5],[20,42]])
    plt.xlabel('Engagement/Followers ratio')
    plt.ylabel('Age')
    file_name = "Hist2D_EngagementFollower_to_Age.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between Pure-NARCISSISM and age"
    plt.hist2d(narcissism_pure,age_pure,5,[[0,1],[20,42]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Age')
    file_name = "Hist2D_pure_narcissism_to_Age.tif" 
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between the number of self posts(in 10 previous posts) (NARCISSISM) and age
    plt.hist2d(narcissism,age_pure,5,[[0,1],[20,42]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Age')
    file_name = "Hist2D_narcissism_to_Age.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between age and the ratio of following/follower"
    plt.hist2d(age_pure,ratio_of_followings_to_followers,5,[[20,42],[0,1]])
    plt.xlabel('Age')
    plt.ylabel('Following/Follower')
    file_name = "Hist2D_Age_to_FollowingFollower.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^^^^^^^^^^^^^^^^^^^^^ Hist2D For Men ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
#---- #Finding the relation between Pure-NARCISSISM and engagement/followers (for men)           
    plt.hist2d(narcissism_pure_m,ratio_of_engagement_to_followers_m,5,[[0,1],[0,1]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Engagement/Followers')
    file_name = "Hist2D_pure_narcissism_to_EngagementFollower_for_men.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between the number of self posts(in 10 previous posts) (NARCISSISM) and engagement/followers (for men)
    plt.hist2d(narcissism_m,ratio_of_engagement_to_followers_m,5,[[0,1],[0,0.5]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Engagement/Followers')
    file_name = "Hist2D_narcissism_to_EngagementFollower_for_men.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
#---- Hist2D : pure-self-presenting/self-presenting & engagement/followers (for men)  
    plt.hist2d(ratio_of_pure_self_presenting_to_self_presenting_m,ratio_of_engagement_to_followers_m,5,[[0,1],[0,1]])
    plt.xlabel('pure_self_presenting/self_presenting ratio')
    plt.ylabel('Engagement/Followers ratio')
    file_name = "Hist2D_pureSF-SF_to_EngagementFollower_for_men.tif" 
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- Hist2D : engagement/followers & following/follower (for men)
    plt.hist2d(ratio_of_engagement_to_followers_m,ratio_of_followings_to_followers_m,5,[[0,0.5],[0,0.5]])
    plt.xlabel('Engagement/Followers ratio')
    plt.ylabel('Following/Follower ratio')
    file_name = "Hist2D_EngagementFollower_to_FollowingFollower_for_men.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- Hist2D : engagement/followers & age (for men)
    plt.hist2d(ratio_of_engagement_to_followers_m,age_pure_m,5,[[0,0.5],[20,42]])
    plt.xlabel('Engagement/Followers ratio')
    plt.ylabel('Age')
    file_name = "Hist2D_EngagementFollower_to_Age_for_men.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between Pure-NARCISSISM and age" (for men)
    plt.hist2d(narcissism_pure_m,age_pure_m,5,[[0,1],[20,42]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Age')
    file_name = "Hist2D_pure_narcissism_to_Age_for_men.tif" 
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between the number of self posts(in 10 previous posts) (NARCISSISM) and age (for men)
    plt.hist2d(narcissism_m,age_pure_m,5,[[0,1],[20,42]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Age')
    file_name = "Hist2D_narcissism_to_Age_for_men.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between age and the ratio of following/follower"  (for men)
    plt.hist2d(age_pure_m,ratio_of_followings_to_followers_m,5,[[20,42],[0,1]])
    plt.xlabel('Age')
    plt.ylabel('Following/Follower')
    file_name = "Hist2D_Age_to_FollowingFollower_for_men.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- Hist2D : pure-self-presenting/self-presenting & following/follower (for men)
    plt.hist2d(ratio_of_pure_self_presenting_to_self_presenting_m,ratio_of_followings_to_followers_m,5,[[0,1],[0,0.5]])
    plt.xlabel('pure_self_presenting/self_presenting ratio')
    plt.ylabel('Following/Follower ratio')
    file_name = "Hist2D_pureSF-SF_to_FollowingFollower_for_men.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between NARCISSISM and the ratio of following/follower" (for men)
    plt.hist2d(narcissism_m,ratio_of_followings_to_followers_m,5,[[0,1],[0,1]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Following/Follower')
    file_name = "Hist2D_narcissism_to_FollowingFollower_for_men.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #finding the relation between Pure-NARCISSISM and the ratio of following/follower" (for men)
    plt.hist2d(narcissism_pure_m,ratio_of_followings_to_followers_m,5,[[0,1],[0,1]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Following/Follower')
    file_name = "Hist2D_pure_narcissism_to_FollowingFollower_for_men.tif" 
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^^^^^^^^^^^^^^^^^^^^^ Hist2D For Women ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
#---- #Finding the relation between Pure-NARCISSISM and engagement/followers (for women)           
    plt.hist2d(narcissism_pure_f,ratio_of_engagement_to_followers_f,5,[[0,1],[0,1]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Engagement/Followers')
    file_name = "Hist2D_pure_narcissism_to_EngagementFollower_for_women.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between the number of self posts(in 10 previous posts) (NARCISSISM) and engagement/followers (for women)
    plt.hist2d(narcissism_f,ratio_of_engagement_to_followers_f,5,[[0,1],[0,0.5]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Engagement/Followers')
    file_name = "Hist2D_narcissism_to_EngagementFollower_for_women.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close() 
#---- Hist2D : pure-self-presenting/self-presenting & engagement/followers (for women)  
    plt.hist2d(ratio_of_pure_self_presenting_to_self_presenting_f,ratio_of_engagement_to_followers_f,5,[[0,1],[0,1]])
    plt.xlabel('pure_self_presenting/self_presenting ratio')
    plt.ylabel('Engagement/Followers ratio')
    file_name = "Hist2D_pureSF-SF_to_EngagementFollower_for_women.tif" 
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- Hist2D : engagement/followers & following/follower (for women)
    plt.hist2d(ratio_of_engagement_to_followers_f,ratio_of_followings_to_followers_f,5,[[0,0.5],[0,0.5]])
    plt.xlabel('Engagement/Followers ratio')
    plt.ylabel('Following/Follower ratio')
    file_name = "Hist2D_EngagementFollower_to_FollowingFollower_for_women.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- Hist2D : engagement/followers & age (for women)
    plt.hist2d(ratio_of_engagement_to_followers_f,age_pure_f,5,[[0,0.5],[20,42]])
    plt.xlabel('Engagement/Followers ratio')
    plt.ylabel('Age')
    file_name = "Hist2D_EngagementFollower_to_Age_for_women.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between Pure-NARCISSISM and age" (for women)
    plt.hist2d(narcissism_pure_f,age_pure_f,5,[[0,1],[20,42]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Age')
    file_name = "Hist2D_pure_narcissism_to_Age_for_women.tif" 
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between the number of self posts(in 10 previous posts) (NARCISSISM) and age (for women)
    plt.hist2d(narcissism_f,age_pure_f,5,[[0,1],[20,42]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Age')
    file_name = "Hist2D_narcissism_to_Age_for_women.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between age and the ratio of following/follower"  (for women)
    plt.hist2d(age_pure_f,ratio_of_followings_to_followers_f,5,[[20,42],[0,1]])
    plt.xlabel('Age')
    plt.ylabel('Following/Follower')
    file_name = "Hist2D_Age_to_FollowingFollower_for_women.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- Hist2D : pure-self-presenting/self-presenting & following/follower (for women)
    plt.hist2d(ratio_of_pure_self_presenting_to_self_presenting_f,ratio_of_followings_to_followers_f,5,[[0,1],[0,0.5]])
    plt.xlabel('pure_self_presenting/self_presenting ratio')
    plt.ylabel('Following/Follower ratio')
    file_name = "Hist2D_pureSF-SF_to_FollowingFollower_for_women.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar()  
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #Finding the relation between NARCISSISM and the ratio of following/follower" (for women)
    plt.hist2d(narcissism_f,ratio_of_followings_to_followers_f,5,[[0,1],[0,1]])
    plt.xlabel('Ratio of self-presenting posts')
    plt.ylabel('Following/Follower')
    file_name = "Hist2D_narcissism_to_FollowingFollower_for_women.tif"  
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()
#---- #finding the relation between Pure-NARCISSISM and the ratio of following/follower" (for women)
    plt.hist2d(narcissism_pure_f,ratio_of_followings_to_followers_f,5,[[0,1],[0,1]])
    plt.xlabel('Ratio of pure self-presenting posts')
    plt.ylabel('Following/Follower')
    file_name = "Hist2D_pure_narcissism_to_FollowingFollower_for_women.tif" 
    path_of_saving = str ("D:\\Papers\\Paper_6") 
    cbar = plt.colorbar() 
    cbar.set_label ("Frequency")
    plt.savefig(os.path.join(path_of_saving, file_name), dpi = 500)
    plt.close()


#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    
    import numpy
    from scipy.stats import pearsonr
    from scipy.stats import spearmanr

    
    ## Correlations General
    #---------------------------------------#
    ## pearson correlation 
    fwtofr_to_litofr = pearsonr(ratio_of_followings_to_followers,ratio_of_likes_to_followers)
    fwtofr_to_cmtofr = pearsonr(ratio_of_followings_to_followers,ratio_of_comment_to_followers)
    fwtofr_to_engtofr = pearsonr(ratio_of_followings_to_followers,ratio_of_engagement_to_followers)
    fwtofr_to_narcissism = pearsonr(ratio_of_followings_to_followers,ratio_of_self_presenting)
    fwtofr_to_pure_narcissism = pearsonr(ratio_of_followings_to_followers,ratio_of_pure_self_presenting)
    fwtofr_to_npn = pearsonr(ratio_of_followings_to_followers,ratio_of_pure_self_presenting_to_self_presenting)
    fwtofr_to_age = pearsonr(ratio_of_followings_to_followers,age_pure)

    litofr_to_narcissism = pearsonr(ratio_of_likes_to_followers,ratio_of_self_presenting)
    litofr_to_pure_narcissism = pearsonr(ratio_of_likes_to_followers,ratio_of_pure_self_presenting)
    litofr_to_npn = pearsonr(ratio_of_likes_to_followers,ratio_of_pure_self_presenting_to_self_presenting)

    engtofr_to_narcissim = pearsonr(ratio_of_engagement_to_followers,ratio_of_self_presenting)
    engtofr_to_pure_narcissism = pearsonr(ratio_of_engagement_to_followers,ratio_of_pure_self_presenting)
    engtofr_to_npn = pearsonr(ratio_of_engagement_to_followers,ratio_of_pure_self_presenting_to_self_presenting)
    engtofr_to_age = pearsonr(ratio_of_engagement_to_followers,age_pure)

    age_to_narcissism = pearsonr(age_pure,ratio_of_self_presenting)
    age_to_pure_narcissism = pearsonr(age_pure,ratio_of_pure_self_presenting)
    age_to_npn = pearsonr(age_pure,ratio_of_pure_self_presenting_to_self_presenting)
    
    # spearman correlation 
    fwtofr_to_litofr_s = spearmanr(ratio_of_followings_to_followers,ratio_of_likes_to_followers)
    fwtofr_to_cmtofr_s = spearmanr(ratio_of_followings_to_followers,ratio_of_comment_to_followers)
    fwtofr_to_engtofr_s = spearmanr(ratio_of_followings_to_followers,ratio_of_engagement_to_followers)
    fwtofr_to_narcissism_s = spearmanr(ratio_of_followings_to_followers,ratio_of_self_presenting)
    fwtofr_to_pure_narcissism_s = spearmanr(ratio_of_followings_to_followers,ratio_of_pure_self_presenting)
    fwtofr_to_npn_s = spearmanr(ratio_of_followings_to_followers,ratio_of_pure_self_presenting_to_self_presenting)
    fwtofr_to_age_s = spearmanr(ratio_of_followings_to_followers,age_pure)
    
    litofr_to_narcissism_s = spearmanr(ratio_of_likes_to_followers,ratio_of_self_presenting)
    litofr_to_pure_narcissism_s = spearmanr(ratio_of_likes_to_followers,ratio_of_pure_self_presenting)
    litofr_to_npn_s = spearmanr(ratio_of_likes_to_followers,ratio_of_pure_self_presenting_to_self_presenting)

    engtofr_to_narcissim_s = spearmanr(ratio_of_engagement_to_followers,ratio_of_self_presenting)
    engtofr_to_pure_narcissism_s = spearmanr(ratio_of_engagement_to_followers,ratio_of_pure_self_presenting)
    engtofr_to_npn_s = spearmanr(ratio_of_engagement_to_followers,ratio_of_pure_self_presenting_to_self_presenting)
    engtofr_to_age_s = spearmanr(ratio_of_engagement_to_followers,age_pure)

    age_to_narcissism_s = spearmanr(age_pure,ratio_of_self_presenting)
    age_to_pure_narcissism_s = spearmanr(age_pure,ratio_of_pure_self_presenting)
    age_to_npn_s = spearmanr(age_pure,ratio_of_pure_self_presenting_to_self_presenting)


    ## Correlations For Men
    #---------------------------------------#
    ## pearson correlation     
    fwtofr_to_engtofr_men = pearsonr(ratio_of_followings_to_followers_m,ratio_of_engagement_to_followers_m)
    fwtofr_to_narcissism_men = pearsonr(ratio_of_followings_to_followers_m,ratio_of_self_presenting_m)
    fwtofr_to_pure_narcissism_men = pearsonr(ratio_of_followings_to_followers_m,ratio_of_pure_self_presenting_m)
    fwtofr_to_npn_men = pearsonr(ratio_of_followings_to_followers_m,ratio_of_pure_self_presenting_to_self_presenting_m)
    fwtofr_to_age_men = pearsonr(ratio_of_followings_to_followers_m,age_pure_m)

    engtofr_to_narcissim_men = pearsonr(ratio_of_engagement_to_followers_m,ratio_of_self_presenting_m)
    engtofr_to_pure_narcissism_men = pearsonr(ratio_of_engagement_to_followers_m,ratio_of_pure_self_presenting_m)
    engtofr_to_npn_men = pearsonr(ratio_of_engagement_to_followers_m,ratio_of_pure_self_presenting_to_self_presenting_m)
    engtofr_to_age_men = pearsonr(ratio_of_engagement_to_followers_m,age_pure_m)

    age_to_narcissism_men = pearsonr(age_pure_m,ratio_of_self_presenting_m)
    age_to_pure_narcissism_men = pearsonr(age_pure_m,ratio_of_pure_self_presenting_m)
    age_to_npn_men = pearsonr(age_pure_m,ratio_of_pure_self_presenting_to_self_presenting_m)
    
    # spearman correlation 
    fwtofr_to_engtofr_s_men = spearmanr(ratio_of_followings_to_followers_m,ratio_of_engagement_to_followers_m)
    fwtofr_to_narcissism_s_men = spearmanr(ratio_of_followings_to_followers_m,ratio_of_self_presenting_m)
    fwtofr_to_pure_narcissism_s_men = spearmanr(ratio_of_followings_to_followers_m,ratio_of_pure_self_presenting_m)
    fwtofr_to_npn_s_men = spearmanr(ratio_of_followings_to_followers_m,ratio_of_pure_self_presenting_to_self_presenting_m)
    fwtofr_to_age_s_men = spearmanr(ratio_of_followings_to_followers_m,age_pure_m)

    engtofr_to_narcissim_s_men = spearmanr(ratio_of_engagement_to_followers_m,ratio_of_self_presenting_m)
    engtofr_to_pure_narcissism_s_men = spearmanr(ratio_of_engagement_to_followers_m,ratio_of_pure_self_presenting_m)
    engtofr_to_npn_s_men = spearmanr(ratio_of_engagement_to_followers_m,ratio_of_pure_self_presenting_to_self_presenting_m)
    engtofr_to_age_s_men = spearmanr(ratio_of_engagement_to_followers_m,age_pure_m)

    age_to_narcissism_s_men = spearmanr(age_pure_m,ratio_of_self_presenting_m)
    age_to_pure_narcissism_s_men = spearmanr(age_pure_m,ratio_of_pure_self_presenting_m)
    age_to_npn_s_men = spearmanr(age_pure_m,ratio_of_pure_self_presenting_to_self_presenting_m)


        ## Correlations For Women
    #---------------------------------------#
    ## pearson correlation     
    fwtofr_to_engtofr_women = pearsonr(ratio_of_followings_to_followers_f,ratio_of_engagement_to_followers_f)
    fwtofr_to_narcissism_women = pearsonr(ratio_of_followings_to_followers_f,ratio_of_self_presenting_f)
    fwtofr_to_pure_narcissism_women = pearsonr(ratio_of_followings_to_followers_f,ratio_of_pure_self_presenting_f)
    fwtofr_to_npn_women = pearsonr(ratio_of_followings_to_followers_f,ratio_of_pure_self_presenting_to_self_presenting_f)
    fwtofr_to_age_women = pearsonr(ratio_of_followings_to_followers_f,age_pure_f)

    engtofr_to_narcissim_women = pearsonr(ratio_of_engagement_to_followers_f,ratio_of_self_presenting_f)
    engtofr_to_pure_narcissism_women = pearsonr(ratio_of_engagement_to_followers_f,ratio_of_pure_self_presenting_f)
    engtofr_to_npn_women = pearsonr(ratio_of_engagement_to_followers_f,ratio_of_pure_self_presenting_to_self_presenting_f)
    engtofr_to_age_women = pearsonr(ratio_of_engagement_to_followers_f,age_pure_f)

    age_to_narcissism_women = pearsonr(age_pure_f,ratio_of_self_presenting_f)
    age_to_pure_narcissism_women = pearsonr(age_pure_f,ratio_of_pure_self_presenting_f)
    age_to_npn_women = pearsonr(age_pure_f,ratio_of_pure_self_presenting_to_self_presenting_f)
    
    # spearman correlation 
    fwtofr_to_engtofr_s_women = spearmanr(ratio_of_followings_to_followers_f,ratio_of_engagement_to_followers_f)
    fwtofr_to_narcissism_s_women = spearmanr(ratio_of_followings_to_followers_f,ratio_of_self_presenting_f)
    fwtofr_to_pure_narcissism_s_women = spearmanr(ratio_of_followings_to_followers_f,ratio_of_pure_self_presenting_f)
    fwtofr_to_npn_s_women = spearmanr(ratio_of_followings_to_followers_f,ratio_of_pure_self_presenting_to_self_presenting_f)
    fwtofr_to_age_s_women = spearmanr(ratio_of_followings_to_followers_f,age_pure_f)

    engtofr_to_narcissim_s_women = spearmanr(ratio_of_engagement_to_followers_f,ratio_of_self_presenting_f)
    engtofr_to_pure_narcissism_s_women = spearmanr(ratio_of_engagement_to_followers_f,ratio_of_pure_self_presenting_f)
    engtofr_to_npn_s_women = spearmanr(ratio_of_engagement_to_followers_f,ratio_of_pure_self_presenting_to_self_presenting_f)
    engtofr_to_age_s_women = spearmanr(ratio_of_engagement_to_followers_f,age_pure_f)

    age_to_narcissism_s_women = spearmanr(age_pure_f,ratio_of_self_presenting_f)
    age_to_pure_narcissism_s_women = spearmanr(age_pure_f,ratio_of_pure_self_presenting_f)
    age_to_npn_s_women = spearmanr(age_pure_f,ratio_of_pure_self_presenting_to_self_presenting_f)

    print (" --------------------------------------------- General Users ------------------------------------------ ")
    print (" ------------------------------------------------ Pearson --------------------------------------------- ")
    print (" fwtofr_to_litofr : ", fwtofr_to_litofr)
    print (" fwtofr_to_cmtofr : ", fwtofr_to_cmtofr)
    print (" fwtofr_to_engtofr : ", fwtofr_to_engtofr)
    print (" fwtofr_to_narcissism : ", fwtofr_to_narcissism)
    print (" fwtofr_to_pure_narcissism : ", fwtofr_to_pure_narcissism)
    print (" fwtofr_to_npn : ", fwtofr_to_npn)
    print (" fwtofr_to_age : ", fwtofr_to_age)
    print (" litofr_to_narcissism : ", litofr_to_narcissism)
    print (" litofr_to_pure_narcissism : ", litofr_to_pure_narcissism)
    print (" litofr_to_npn : ", litofr_to_npn)    
    print (" engtofr_to_narcissim : ", engtofr_to_narcissim)
    print (" engtofr_to_pure_narcissism : ", engtofr_to_pure_narcissism)
    print (" engtofr_to_npn : ", engtofr_to_npn)
    print (" engtofr_to_age : ", engtofr_to_age)
    print (" age_to_narcissism : ", age_to_narcissism)
    print (" age_to_pure_narcissism : ", age_to_pure_narcissism)
    print (" age_to_npn : ", age_to_npn)    
    print (" --------------------------------------------------------------------------------------------------------------------- ")
    print (" ------------------------------------ Spearman ------------------------------------ ")
    print (" fwtofr_to_litofr_s : ", fwtofr_to_litofr_s)
    print (" fwtofr_to_cmtofr_s : ", fwtofr_to_cmtofr_s)
    print (" fwtofr_to_engtofr_s : ", fwtofr_to_engtofr_s)
    print (" fwtofr_to_narcissism_s : ", fwtofr_to_narcissism_s)
    print (" fwtofr_to_pure_narcissism_s : ", fwtofr_to_pure_narcissism_s)
    print (" fwtofr_to_npn_s : ", fwtofr_to_npn_s)
    print (" fwtofr_to_age_s : ", fwtofr_to_age_s)
    print (" litofr_to_narcissism_s : ", litofr_to_narcissism_s)
    print (" litofr_to_pure_narcissism_s : ", litofr_to_pure_narcissism_s)
    print (" litofr_to_npn_s : ", litofr_to_npn_s)    
    print (" engtofr_to_narcissim_s : ", engtofr_to_narcissim_s)
    print (" engtofr_to_pure_narcissism_s : ", engtofr_to_pure_narcissism_s)
    print (" engtofr_to_npn_s : ", engtofr_to_npn_s)
    print (" engtofr_to_age_s : ", engtofr_to_age_s)
    print (" age_to_narcissism_s : ", age_to_narcissism_s)
    print (" age_to_pure_narcissism_s : ", age_to_pure_narcissism_s)
    print (" age_to_npn_s : ", age_to_npn_s)

    print (" --------------------------------------------- Men Users ---------------------------------------------- ")
    print (" ------------------------------------------------ Pearson --------------------------------------------- ")
    print (" fwtofr_to_engtofr_men : ", fwtofr_to_engtofr_men)
    print (" fwtofr_to_narcissism_men : ", fwtofr_to_narcissism_men)
    print (" fwtofr_to_pure_narcissism_men : ", fwtofr_to_pure_narcissism_men)
    print (" fwtofr_to_npn_men : ", fwtofr_to_npn_men)
    print (" fwtofr_to_age_men : ", fwtofr_to_age_men)    
    print (" engtofr_to_narcissim_men : ", engtofr_to_narcissim_men)
    print (" engtofr_to_pure_narcissism_men : ", engtofr_to_pure_narcissism_men)
    print (" engtofr_to_npn_men : ", engtofr_to_npn_men)
    print (" engtofr_to_age_men : ", engtofr_to_age_men)
    print (" age_to_narcissism_men : ", age_to_narcissism_men)
    print (" age_to_pure_narcissism_men : ", age_to_pure_narcissism_men)
    print (" age_to_npn_men : ", age_to_npn_men)    
    print (" --------------------------------------------------------------------------------------------------------------------- ")
    print (" ------------------------------------ Spearman ------------------------------------ ")
    print (" fwtofr_to_engtofr_s_men : ", fwtofr_to_engtofr_s_men)
    print (" fwtofr_to_narcissism_s_men : ", fwtofr_to_narcissism_s_men)
    print (" fwtofr_to_pure_narcissism_s_men : ", fwtofr_to_pure_narcissism_s_men)
    print (" fwtofr_to_npn_s_men : ", fwtofr_to_npn_s_men)
    print (" fwtofr_to_age_s_men : ", fwtofr_to_age_s_men)    
    print (" engtofr_to_narcissim_s_men : ", engtofr_to_narcissim_s_men)
    print (" engtofr_to_pure_narcissism_s_men : ", engtofr_to_pure_narcissism_s_men)
    print (" engtofr_to_npn_s_men : ", engtofr_to_npn_s_men)
    print (" engtofr_to_age_s_men : ", engtofr_to_age_s_men)
    print (" age_to_narcissism_s_men : ", age_to_narcissism_s_men)
    print (" age_to_pure_narcissism_s_men : ", age_to_pure_narcissism_s_men)
    print (" age_to_npn_s_men : ", age_to_npn_s_men)
    print (" --------------------------------------------- Women Users -------------------------------------------- ")
    print (" ------------------------------------------------ Pearson --------------------------------------------- ")
    print (" fwtofr_to_engtofr_women : ", fwtofr_to_engtofr_women)
    print (" fwtofr_to_narcissism_women : ", fwtofr_to_narcissism_women)
    print (" fwtofr_to_pure_narcissism_women : ", fwtofr_to_pure_narcissism_women)
    print (" fwtofr_to_npn_women : ", fwtofr_to_npn_women)
    print (" fwtofr_to_age_women : ", fwtofr_to_age_women)    
    print (" engtofr_to_narcissim_women : ", engtofr_to_narcissim_women)
    print (" engtofr_to_pure_narcissism_women : ", engtofr_to_pure_narcissism_women)
    print (" engtofr_to_npn_women : ", engtofr_to_npn_women)
    print (" engtofr_to_age_women : ", engtofr_to_age_women)
    print (" age_to_narcissism_women : ", age_to_narcissism_women)
    print (" age_to_pure_narcissism_women : ", age_to_pure_narcissism_women)
    print (" age_to_npn_women : ", age_to_npn_women)    
    print (" --------------------------------------------------------------------------------------------------------------------- ")
    print (" ------------------------------------ Spearman ------------------------------------ ")
    print (" fwtofr_to_engtofr_s_women : ", fwtofr_to_engtofr_s_women)
    print (" fwtofr_to_narcissism_s_women : ", fwtofr_to_narcissism_s_women)
    print (" fwtofr_to_pure_narcissism_s_women : ", fwtofr_to_pure_narcissism_s_women)
    print (" fwtofr_to_npn_s_women : ", fwtofr_to_npn_s_women)
    print (" fwtofr_to_age_s_women : ", fwtofr_to_age_s_women)   
    print (" engtofr_to_narcissim_s_women : ", engtofr_to_narcissim_s_women)
    print (" engtofr_to_pure_narcissism_s_women : ", engtofr_to_pure_narcissism_s_women)
    print (" engtofr_to_npn_s_women : ", engtofr_to_npn_s_women)
    print (" engtofr_to_age_s_women : ", engtofr_to_age_s_women)
    print (" age_to_narcissism_s_women : ", age_to_narcissism_s_women)
    print (" age_to_pure_narcissism_s_women : ", age_to_pure_narcissism_s_women)
    print (" age_to_npn_s_women : ", age_to_npn_s_women)
    
#--------------------
main()
input("\n press enter key to exit.")
