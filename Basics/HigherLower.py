import random

data = [
    {
        "name": "JaneDoe",
        "followers": 120000,
        "description": "Travel blogger sharing adventures around the world.",
        "country": "United States"
    },
    {
        "name": "FoodieLife",
        "followers": 85000,
        "description": "Delicious recipes and food reviews.",
        "country": "Canada"
    },
    {
        "name": "FitAndStrong",
        "followers": 200000,
        "description": "Fitness tips, workouts, and healthy lifestyle inspiration.",
        "country": "Australia"
    },
    {
        "name": "ArtVibes",
        "followers": 50000,
        "description": "Showcasing amazing art and design from around the world.",
        "country": "United Kingdom"
    },
    {
        "name": "TechGuru",
        "followers": 150000,
        "description": "Latest tech trends, gadgets, and tutorials.",
        "country": "India"
    },
    {
        "name": "NatureNook",
        "followers": 75000,
        "description": "Capturing the beauty of nature and wildlife.",
        "country": "South Africa"
    },
    {
        "name": "FashionForward",
        "followers": 180000,
        "description": "Exploring the latest trends in fashion and style.",
        "country": "France"
    },
    {
        "name": "PetLover",
        "followers": 60000,
        "description": "Adorable pet pictures and animal care tips.",
        "country": "Germany"
    },
    {
        "name": "LifeCoach",
        "followers": 95000,
        "description": "Motivational quotes and personal growth strategies.",
        "country": "Brazil"
    },
    {
        "name": "GamerZone",
        "followers": 140000,
        "description": "Gaming tips, walkthroughs, and esports updates.",
        "country": "Japan"
    },
    {
        "name": "DIYDreams",
        "followers": 40000,
        "description": "Creative DIY projects and crafting tutorials.",
        "country": "Italy"
    },
    {
        "name": "AdventureSeekers",
        "followers": 170000,
        "description": "Extreme sports and outdoor adventures.",
        "country": "New Zealand"
    },
    {
        "name": "HealthyEats",
        "followers": 115000,
        "description": "Sharing healthy recipes and nutrition advice.",
        "country": "Spain"
    },
    {
        "name": "BookWorm",
        "followers": 30000,
        "description": "Reviews and recommendations for book lovers.",
        "country": "Netherlands"
    },
    {
        "name": "UrbanExplorer",
        "followers": 90000,
        "description": "Discovering hidden gems in cities worldwide.",
        "country": "Singapore"
    }
]

curr_score = 0

rand1 = random.randint(0, 14)

def compare(rand1):
    global curr_score
    rand2 = random.randint(0, 14)

    print(f"Compare A: {data[rand1]['name']}, {data[rand1]['description']}, {data[rand1]['country']}")
    print("\nVS\n")
    print(f"Compare B: {data[rand2]['name']}, {data[rand2]['description']}, {data[rand2]['country']}")
    
    guess = input("\nWho has more followers? Type 'A' or 'B': ")

    if data[rand1]['followers'] > data[rand2]['followers']:
        if guess == "A" :
            curr_score +=1
            print("\n" * 20)
            print(f"You are right, current score: {curr_score}.")
            compare(rand1)
        else:
            print(f"Sorry, that's wrong, Final score: {curr_score}")
    else:
        if guess == "B" :
            curr_score +=1
            print("\n" * 20)
            print(f"You are right, current score: {curr_score}.")
            compare(rand2)
        else:
            print(f"\nSorry, that's wrong, Final score: {curr_score}")

compare(rand1)