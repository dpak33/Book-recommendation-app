import random

# Mock database of books
BOOK_DATABASE = [
    {"title": "To Kill a Mockingbird", "categories": ["fiction", "classic"], "description": "A novel about racism and injustice."},
    {"title": "1984", "categories": ["fiction", "dystopia"], "description": "A novel about a totalitarian regime."},
    {"title": "Pride and Prejudice", "categories": ["fiction", "romance"], "description": "A novel about love and society."},
    {"title": "Dune", "categories": ["fiction", "science fiction"], "description": "A novel about a desert planet and its resources."},
    {"title": "Ender's Game", "categories": ["fiction", "science fiction"], "description": "A novel about a young boy trained to be a military leader in space."},
    {"title": "Foundation", "categories": ["fiction", "science fiction"], "description": "A novel about the fall and rise of a galactic empire."},
    {"title": "Neuromancer", "categories": ["fiction", "cyberpunk"], "description": "A novel about a washed-up computer hacker hired for a final job."},
    {"title": "Snow Crash", "categories": ["fiction", "cyberpunk"], "description": "A novel about a computer virus that infects both humans and machines."},
    {"title": "The Martian", "categories": ["fiction", "science fiction"], "description": "A novel about an astronaut stranded on Mars."},
    {"title": "Ready Player One", "categories": ["fiction", "science fiction"], "description": "A novel about a virtual reality treasure hunt."},
    {"title": "The Left Hand of Darkness", "categories": ["fiction", "science fiction"], "description": "A novel about a planet with a unique gender system."},
    {"title": "Hyperion", "categories": ["fiction", "science fiction"], "description": "A novel about seven pilgrims on a journey to meet the Shrike."},
    {"title": "The Expanse", "categories": ["fiction", "science fiction"], "description": "A novel about a conspiracy that threatens the solar system."},
    {"title": "American Gods", "categories": ["fiction", "fantasy"], "description": "A novel about a man caught in a war between old and new gods."},
    {"title": "Good Omens", "categories": ["fiction", "fantasy"], "description": "A novel about an angel and a demon teaming up to prevent the apocalypse."},
    {"title": "The Name of the Wind", "categories": ["fiction", "fantasy"], "description": "A novel about the life and adventures of a legendary figure."},
    {"title": "The Lies of Locke Lamora", "categories": ["fiction", "fantasy"], "description": "A novel about a group of thieves in a fantastical city."},
    {"title": "Mistborn", "categories": ["fiction", "fantasy"], "description": "A novel about a young woman who discovers her magical abilities."},
    {"title": "The Way of Kings", "categories": ["fiction", "fantasy"], "description": "A novel about a world torn apart by magical storms."},
    {"title": "A Game of Thrones", "categories": ["fiction", "fantasy"], "description": "A novel about the political and military struggles in a medieval-like world."},
    {"title": "The Once and Future King", "categories": ["fiction", "fantasy"], "description": "A novel about the legend of King Arthur."},
    {"title": "The Sword of Shannara", "categories": ["fiction", "fantasy"], "description": "A novel about a young man on a quest to save the world from an ancient evil."},
    {"title": "Elantris", "categories": ["fiction", "fantasy"], "description": "A novel about a city of once-magic-wielding people who are now cursed."},
    {"title": "Fahrenheit 451", "categories": ["fiction", "dystopia"], "description": "A novel about a future society where books are banned and 'firemen' burn them."},
    {"title": "The Giver", "categories": ["fiction", "dystopia"], "description": "A novel about a boy who learns the dark secrets of his seemingly perfect society."},
    {"title": "Animal Farm", "categories": ["fiction", "satire"], "description": "A novel about a group of farm animals who overthrow their human owner."},
    {"title": "Lord of the Flies", "categories": ["fiction", "classic"], "description": "A novel about a group of boys stranded on an uninhabited island."},
    {"title": "Catch-22", "categories": ["fiction", "satire"], "description": "A novel about the absurdities of war."},
    {"title": "One Hundred Years of Solitude", "categories": ["fiction", "magical realism"], "description": "A novel about the multi-generational story of the Buendía family."},
    {"title": "Beloved", "categories": ["fiction", "historical"], "description": "A novel about a runaway slave haunted by the ghost of her dead daughter."},
    {"title": "Invisible Man", "categories": ["fiction", "classic"], "description": "A novel about an African American man's social invisibility."},
    {"title": "The Catcher in the Rye", "categories": ["fiction", "classic"], "description": "A novel about teenage angst and alienation."},
    {"title": "Slaughterhouse-Five", "categories": ["fiction", "satire"], "description": "A novel about the bombing of Dresden during WWII."},
    {"title": "1984", "categories": ["fiction", "dystopia"], "description": "A novel about a totalitarian regime."},
    {"title": "Brave New World", "categories": ["fiction", "dystopia"], "description": "A novel about a futuristic society driven by technological advancements."},
    {"title": "Frankenstein", "categories": ["fiction", "horror"], "description": "A novel about a scientist who creates a monstrous being."},
    {"title": "Dracula", "categories": ["fiction", "horror"], "description": "A novel about the vampire Count Dracula's attempt to move to England."},
    {"title": "The Road", "categories": ["fiction", "post-apocalyptic"], "description": "A novel about a father and son's journey through a desolate America."},
    {"title": "The Handmaid's Tale", "categories": ["fiction", "dystopia"], "description": "A novel about a woman's life in a totalitarian society."},
    {"title": "The Hunger Games", "categories": ["fiction", "dystopia"], "description": "A novel about a girl fighting for survival in a televised death match."},
    {"title": "Divergent", "categories": ["fiction", "dystopia"], "description": "A novel about a society divided into factions based on human virtues."},
    {"title": "The Maze Runner", "categories": ["fiction", "dystopia"], "description": "A novel about boys trapped in a mysterious and deadly maze."},
    {"title": "Percy Jackson & The Olympians", "categories": ["fiction", "fantasy"], "description": "A novel about a boy discovering he is the son of a Greek god."},
    {"title": "Eragon", "categories": ["fiction", "fantasy"], "description": "A novel about a boy who finds a dragon egg and becomes a dragon rider."},
    {"title": "To Kill a Mockingbird", "categories": ["fiction", "classic"], "description": "A novel about racism and injustice."},
    {"title": "1984", "categories": ["fiction", "dystopia"], "description": "A novel about a totalitarian regime."},
    {"title": "Pride and Prejudice", "categories": ["fiction", "romance"], "description": "A novel about love and society."},
    {"title": "The Great Gatsby", "categories": ["fiction", "classic"], "description": "A novel about the American dream and disillusionment."},
    {"title": "Moby Dick", "categories": ["fiction", "adventure"], "description": "A novel about the quest for revenge against the white whale."},
    {"title": "The Catcher in the Rye", "categories": ["fiction", "classic"], "description": "A novel about teenage angst and alienation."},
    {"title": "Brave New World", "categories": ["fiction", "dystopia"], "description": "A novel about a futuristic society driven by technological advancements."},
    {"title": "Jane Eyre", "categories": ["fiction", "romance"], "description": "A novel about the life and struggles of an orphaned girl."},
    {"title": "Wuthering Heights", "categories": ["fiction", "romance"], "description": "A novel about love and revenge on the Yorkshire moors."},
    {"title": "The Hobbit", "categories": ["fiction", "fantasy"], "description": "A novel about the adventures of Bilbo Baggins."},
    {"title": "The Lord of the Rings", "categories": ["fiction", "fantasy"], "description": "A novel about the quest to destroy the One Ring."},
    {"title": "Harry Potter and the Sorcerer's Stone", "categories": ["fiction", "fantasy"], "description": "A novel about a young wizard's first year at Hogwarts."},
    {"title": "The Chronicles of Narnia", "categories": ["fiction", "fantasy"], "description": "A novel about children discovering a magical world."},
    {"title": "Alice's Adventures in Wonderland", "categories": ["fiction", "fantasy"], "description": "A novel about a girl's journey through a fantastical world."},
    {"title": "The Da Vinci Code", "categories": ["fiction", "mystery"], "description": "A novel about a symbologist uncovering secrets of the Catholic Church."},
    {"title": "The Girl with the Dragon Tattoo", "categories": ["fiction", "mystery"], "description": "A novel about a journalist and a hacker solving a family mystery."},
    {"title": "Gone Girl", "categories": ["fiction", "thriller"], "description": "A novel about the disappearance of a woman and the ensuing investigation."},
    {"title": "The Shining", "categories": ["fiction", "horror"], "description": "A novel about a family's terrifying experience in a haunted hotel."},
    {"title": "Dracula", "categories": ["fiction", "horror"], "description": "A novel about the vampire Count Dracula's attempt to move to England."},
    {"title": "Frankenstein", "categories": ["fiction", "horror"], "description": "A novel about a scientist who creates a monstrous being."},
    {"title": "The Road", "categories": ["fiction", "post-apocalyptic"], "description": "A novel about a father and son's journey through a desolate America."},
    {"title": "The Handmaid's Tale", "categories": ["fiction", "dystopia"], "description": "A novel about a woman's life in a totalitarian society."},
    {"title": "The Hunger Games", "categories": ["fiction", "dystopia"], "description": "A novel about a girl fighting for survival in a televised death match."},
    {"title": "Divergent", "categories": ["fiction", "dystopia"], "description": "A novel about a society divided into factions based on human virtues."},
    {"title": "The Maze Runner", "categories": ["fiction", "dystopia"], "description": "A novel about boys trapped in a mysterious and deadly maze."},
    {"title": "Percy Jackson & The Olympians", "categories": ["fiction", "fantasy"], "description": "A novel about a boy discovering he is the son of a Greek god."},
    {"title": "Eragon", "categories": ["fiction", "fantasy"], "description": "A novel about a boy who finds a dragon egg and becomes a dragon rider."},
    {"title": "The Book Thief", "categories": ["fiction", "historical"], "description": "A novel about a young girl's experience in Nazi Germany."},
    {"title": "All the Light We Cannot See", "categories": ["fiction", "historical"], "description": "A novel about a blind French girl and a German boy in WWII."},
    {"title": "The Nightingale", "categories": ["fiction", "historical"], "description": "A novel about two sisters' experiences in Nazi-occupied France."},
    {"title": "The Help", "categories": ["fiction", "historical"], "description": "A novel about African American maids working in white households in the 1960s."},
    {"title": "Memoirs of a Geisha", "categories": ["fiction", "historical"], "description": "A novel about the life of a geisha in Japan."},
    {"title": "The Kite Runner", "categories": ["fiction", "historical"], "description": "A novel about a boy's friendship and betrayal in Afghanistan."},
    {"title": "Life of Pi", "categories": ["fiction", "adventure"], "description": "A novel about a boy's survival at sea with a Bengal tiger."},
    {"title": "The Alchemist", "categories": ["fiction", "philosophical"], "description": "A novel about a shepherd's journey to find a hidden treasure."},
    {"title": "Siddhartha", "categories": ["fiction", "philosophical"], "description": "A novel about a man's spiritual journey in ancient India."},
    {"title": "Catch-22", "categories": ["fiction", "satire"], "description": "A novel about the absurdities of war."},
    {"title": "Slaughterhouse-Five", "categories": ["fiction", "satire"], "description": "A novel about the bombing of Dresden during WWII."},
    {"title": "The Hitchhiker's Guide to the Galaxy", "categories": ["fiction", "science fiction"], "description": "A novel about a man's adventures in space."},
    {"title": "Sapiens: A Brief History of Humankind", "categories": ["non-fiction", "history"], "description": "A book exploring the history of the human species."},
    {"title": "Educated", "categories": ["non-fiction", "memoir"], "description": "A memoir about a woman who grows up in a strict and abusive household in rural Idaho but eventually escapes to learn about the wider world through education."},
    {"title": "The Immortal Life of Henrietta Lacks", "categories": ["non-fiction", "biography"], "description": "The story of a woman whose cells were used to create the first immortal human cell line."},
    {"title": "Thinking, Fast and Slow", "categories": ["non-fiction", "psychology"], "description": "A book that delves into the two systems of thought that drive the way we think."},
    {"title": "The Wright Brothers", "categories": ["non-fiction", "biography"], "description": "A biography of the inventors of the first successful airplane."},
    {"title": "The Power of Habit", "categories": ["non-fiction", "self-help"], "description": "A book that explores the science behind why habits exist and how they can be changed."},
    {"title": "Outliers: The Story of Success", "categories": ["non-fiction", "psychology"], "description": "A book that examines the factors that contribute to high levels of success."},
    {"title": "Into the Wild", "categories": ["non-fiction", "biography"], "description": "The story of a young man who gives up all his possessions and savings to live in the Alaskan wilderness."},
    {"title": "Unbroken: A World War II Story of Survival, Resilience, and Redemption", "categories": ["non-fiction", "biography"], "description": "A biography of an Olympic runner who becomes a World War II bombardier and is captured by the Japanese."},
    {"title": "Guns, Germs, and Steel: The Fates of Human Societies", "categories": ["non-fiction", "history"], "description": "A book that explores the factors that have shaped human history."},
    {"title": "The Sixth Extinction: An Unnatural History", "categories": ["non-fiction", "science"], "description": "A book about the ongoing sixth mass extinction caused by human activity."},
    {"title": "Silent Spring", "categories": ["non-fiction", "environment"], "description": "A book that brought environmental concerns to the American public."},
    {"title": "The Emperor of All Maladies: A Biography of Cancer", "categories": ["non-fiction", "medical"], "description": "A comprehensive history of cancer and its treatment."},
    {"title": "The Man Who Mistook His Wife for a Hat", "categories": ["non-fiction", "psychology"], "description": "A collection of case studies about people with neurological disorders."},
    {"title": "Surely You're Joking, Mr. Feynman!", "categories": ["non-fiction", "autobiography"], "description": "Adventures of a curious character as told by a Nobel Prize-winning physicist."},
    {"title": "Bad Blood: Secrets and Lies in a Silicon Valley Startup", "categories": ["non-fiction", "business"], "description": "The story of the rise and fall of Theranos and its founder, Elizabeth Holmes."},
    {"title": "The Tipping Point: How Little Things Can Make a Big Difference", "categories": ["non-fiction", "sociology"], "description": "A book that explores how small actions can create a tipping point for social change."},
    {"title": "Freakonomics: A Rogue Economist Explores the Hidden Side of Everything", "categories": ["non-fiction", "economics"], "description": "A book that applies economic theory to diverse subjects not usually covered by traditional economists."},
    {"title": "The Soul of a New Machine", "categories": ["non-fiction", "technology"], "description": "A book about the creation of a new computer at a major American computer company."},
    {"title": "In Cold Blood", "categories": ["non-fiction", "true crime"], "description": "A detailed account of the murder of a Kansas family and the investigation that followed."},
    {"title": "Bossypants", "categories": ["non-fiction", "memoir"], "description": "A memoir by comedian Tina Fey."},
    {"title": "Wild: From Lost to Found on the Pacific Crest Trail", "categories": ["non-fiction", "memoir"], "description": "A memoir about a woman's solo hike on the Pacific Crest Trail."},
    {"title": "When Breath Becomes Air", "categories": ["non-fiction", "memoir"], "description": "A memoir by a neurosurgeon who faced terminal cancer."},
    {"title": "The Devil in the White City: Murder, Magic, and Madness at the Fair That Changed America", "categories": ["non-fiction", "history"], "description": "A book that intertwines the true tale of the 1893 World's Fair with that of a serial killer."},
    {"title": "The Glass Castle", "categories": ["non-fiction", "memoir"], "description": "A memoir about growing up in a dysfunctional family."},
    {"title": "Hidden Figures", "categories": ["non-fiction", "history"], "description": "The story of the African American women mathematicians who helped win the space race."},
    {"title": "Just Mercy: A Story of Justice and Redemption", "categories": ["non-fiction", "law"], "description": "A memoir by a lawyer dedicated to defending those most desperate and in need."},
    {"title": "Team of Rivals: The Political Genius of Abraham Lincoln", "categories": ["non-fiction", "biography"], "description": "A biography that highlights Lincoln's political acumen."},
    {"title": "The Art of War", "categories": ["non-fiction", "strategy"], "description": "An ancient Chinese military treatise."},
    {"title": "On Writing: A Memoir of the Craft", "categories": ["non-fiction", "memoir"], "description": "A memoir by Stephen King that also includes a guide to writing."},
    {"title": "The New Jim Crow: Mass Incarceration in the Age of Colorblindness", "categories": ["non-fiction", "sociology"], "description": "A book that discusses the social and legal issues surrounding mass incarceration in the United States."},
    {"title": "Quiet: The Power of Introverts in a World That Can't Stop Talking", "categories": ["non-fiction", "psychology"], "description": "A book that explores the power and value of introverts."},
    {"title": "Why We Sleep: Unlocking the Power of Sleep and Dreams", "categories": ["non-fiction", "science"], "description": "A book about the science of sleep and how it affects our lives."},
    {"title": "Blink: The Power of Thinking Without Thinking", "categories": ["non-fiction", "psychology"], "description": "A book about the power of snap judgments and intuitive thinking."},
    {"title": "Man's Search for Meaning", "categories": ["non-fiction", "psychology"], "description": "A book by a Holocaust survivor about finding meaning in life."},
    {"title": "Into Thin Air: A Personal Account of the Mount Everest Disaster", "categories": ["non-fiction", "memoir"], "description": "A personal account of the 1996 Mount Everest disaster."},
    {"title": "Black Like Me", "categories": ["non-fiction", "sociology"], "description": "A book about a white journalist who disguised himself as a Black man to understand racial segregation."},
    {"title": "Nickel and Dimed: On (Not) Getting By in America", "categories": ["non-fiction", "economics"], "description": "A book about living and working in low-wage America."},
    {"title": "The Omnivore's Dilemma: A Natural History of Four Meals", "categories": ["non-fiction", "food"], "description": "A book that explores the food choices we face and their consequences."},
    {"title": "Evicted: Poverty and Profit in the American City", "categories": ["non-fiction", "sociology"], "description": "A book about the lives of eight families as they struggle to keep a roof over their heads."}
]

def recommend_books(category_features, description_features):
    recommendations = []

    for book in BOOK_DATABASE:
        if (
            any(feature in book["categories"] for feature in category_features) or
            any(feature in book["description"].lower() for feature in description_features)
        ):
            recommendations.append(book)
    
    if not recommendations:
        # If no matches, return random recommendations
        recommendations = random.sample(BOOK_DATABASE, 3)
    
    return recommendations