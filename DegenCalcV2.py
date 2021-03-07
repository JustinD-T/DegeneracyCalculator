# Imports
import json
import requests as req
# Checks Username and produces ping URL
UserCheck = "yourmom"
while UserCheck != "Yes" and UserCheck != "yes":
    print("User is case sensitive!")
    User = input("Please enter your My Anime List Username :   ")
    print(User + "?")
    UserCheck = input("Is this correct? Type 'Yes' or 'No'")

# Sets variuble as 0, since we haven't read any anime yet, the index starts at 0 + sets main data list
MediaOffset = 0
BigData = []
while True:
    URL = "https://api.myanimelist.net/v2/users/"+User+"/animelist?offset="+str(MediaOffset)+"&fields=mean%2Cnum_episodes%2Caverage_episode_duration%2Crating&status=completed"
    # Gets raw account data and stores in variuble
    hed={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjRmOTQ2MjZhMmZjNTI0NTNmN2M3YzlmODE0NmRmMTg1ODg1N2E5ZmRhYjk1NWRmYmQ0ZDVhYmRkNGQyZmU2N2FmYTM0NzM2YjhmODgyODI2In0.eyJhdWQiOiJlNDVmNTZlNTVlY2NiNjU4ZmIwNTRmZjJlNTJmMWFmOCIsImp0aSI6IjRmOTQ2MjZhMmZjNTI0NTNmN2M3YzlmODE0NmRmMTg1ODg1N2E5ZmRhYjk1NWRmYmQ0ZDVhYmRkNGQyZmU2N2FmYTM0NzM2YjhmODgyODI2IiwiaWF0IjoxNjE1MDQ4NjQzLCJuYmYiOjE2MTUwNDg2NDMsImV4cCI6MTYxNzcyMzQ0Miwic3ViIjoiMTIwMjAwNTAiLCJzY29wZXMiOltdfQ.TYAbqNHy8x4b_bp_h5zf19DQ9ulxlOhRilkSmLiWSh8H7lLY-HHIHWBo7RJIC79We6_kyjyIRxcfS-_xcCNOxtxUZTuv2C80Oplihw0Jmovl6gSertBot9zAKe9fSmq7_cVESOTQ3x6Hh2uQRcsAqjZLdWsB8LGS-x4vAkmYEjmZBSCsZDPvOBicq-MnP9AnVAQECEbnz_YqqkQGGX708wJcMYPK1MYmSV38Ype83wyGfxNGQ2iUryXx6_RAQ8wlaEo_4tIPJiWyQxRl7GgzSElvSf9DxzMvTinvKjIALRZk5yf3LKDeFBQ3Oxyrd4ImDOVrhf69qwegRQDyufEtXQ'}
    TempRawData = req.get(URL,headers = hed)
    PreParsedData = json.loads(TempRawData.text)
    ParsedData = PreParsedData["data"]
    BigData = BigData + ParsedData 
    MediaOffset = MediaOffset + 10
    if len(ParsedData) == 0:
        break
# FLAG: CHANGE ALL 'PARSED DATA VARUIBLES to BigData'
# Collecting and storing important variubles for each anime
    # Finding and storing number of anime
NodeLength = len(BigData)
    # Prepping varuibles for the while loop
AnimeIndex = 0
MeanList = []
DurationList = []
EpisodesList = []
    # Recording each varuible and storing into list
while AnimeIndex < NodeLength:
    MeanList.append(BigData[AnimeIndex]["node"]["mean"])
    DurationList.append(BigData[AnimeIndex]["node"]["average_episode_duration"])
    EpisodesList.append(BigData[AnimeIndex]["node"]["num_episodes"])
    AnimeIndex = AnimeIndex + 1
# Making and Calculating stats
    # Calculating Average Score
SumScore = 0
for Score in MeanList:
    SumScore = SumScore + Score
AverageScore = SumScore / NodeLength
# print(AverageScore)
    # Total time watched anime
TotalTimeMinutes = 0
for TimeCurrentIndex in range(NodeLength):
    TempTimeTotal = (DurationList[TimeCurrentIndex]) * (EpisodesList[TimeCurrentIndex]) / 60
    TotalTimeMinutes = TotalTimeMinutes + TempTimeTotal
# FLAG: add remeinder in minutes rather than decimal
TotalTime = TotalTimeMinutes / 60
# Total episodes watched
TotalEpisodesWatched = 0
for Episodes in EpisodesList:
    TotalEpisodesWatched = TotalEpisodesWatched + Episodes
# Longest Anime Watched
AnimeLengthList = []
for TimePerAnimeIndex in range(NodeLength):
    TempAnimeLength = (DurationList[TimePerAnimeIndex]) * (EpisodesList[TimePerAnimeIndex])
    AnimeLengthList.append(TempAnimeLength)
LongestAnimeLengthHours = max(AnimeLengthList) / 60 / 60
AnimeLengthIndexCommandNumber = max(AnimeLengthList)
AnimeLengthFetchIndex = AnimeLengthList.index(AnimeLengthIndexCommandNumber)
LongestAnimeTitle = BigData[AnimeLengthFetchIndex]["node"]["title"]
print(LongestAnimeLengthHours)
# For stats calculated, we have 1. average score 2. total time spent watching anime 3. total episodes watched
# FLAG: change the initial if statements, they are just there to make sure that it's collapsible
print("The average score of all the anime you've watched is:   "+str(AverageScore)+"!")
if AverageScore > -1:
    if AverageScore == 10:
        print("Bullshit, there aren't even any anime on MAL with 10.00 rating!")
    elif AverageScore >= 9:
        print("Wow, you truly are a connesiuer of fine anime, please bestow us mortals with you lack of degeneracy!")
    elif AverageScore >= 8:
        print("You are a person great anime taste, congrats. You are still a degenerate though, there is no escape from that...")
    elif AverageScore >= 7:
        print("Congrats... You are perfectally average. Though sadly for you, the title of an 'average' weeb does not bode well...")
    elif AverageScore >= 6:
        print("C'mon dude, you are BELOW average for a weeb. Luckily for you, you haven't past the point of no return; if you start watching non-degen content you can be saved!")
    elif AverageScore >= 5:
        print("I don't know how you even make it this low, this is a joke account right... For dear god I hope so. Please... just delete your account at this point - There is no return from this")
    elif AverageScore >= 4:
        print("Ouch, I didn't think (and hoped) that this part of the code would ever be used. I don't even understand, either you have a supreme taste for trash anime... or this is your NSFW accuont used for keeping track of Hentai you peice of human filth. ")
print("The total time you've spent watching anime is:   "+str(TotalTime)+"Hrs")
# First, find average numbers to base this around.
# if TotalTime > -1:
#     if TotalTime > Ultra High
#     elif TotalTime > High
#     elif TotalTime > normal
#     elif TotalTime > low
#     elif TotalTime > ultra low
print("The total number of episodes you've watched is:   "+str(TotalEpisodesWatched)+"!")
# First, find average numbers to base this around.
# if TotalTime > -1:
#     if TotalTime > Ultra High
#     elif TotalTime > High
#     elif TotalTime > normal
#     elif TotalTime > low
#     elif TotalTime > ultra low
print("The longest anime you've watched is:   "+str(LongestAnimeTitle)+", with a total of "+str(LongestAnimeLengthHours)+"hrs. Jesus, thats a LOT of filler!")




# print("Mean Scores:   ")
# print(MeanList)
# print("Episode Duration:   ")
# print(DurationList)
# print("Number of Episodes:   ")
# print(EpisodesList)




# Mean = ParsedData["data"][0]["node"]["mean"]
