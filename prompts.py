from langchain_core.prompts import PromptTemplate


meal_prompt = PromptTemplate(
    template="""
You are a certified nutritionist AI.

Create a personalized daily meal plan based on the following user data:
Age: {age}
Weight: {weight}
Height: {height}
Activity Level: {activity}
Dietary Preference: {diet}
Fitness Goal: {goal}

Requirements:
- Include Breakfast, Lunch, Dinner, and Snacks
- Mention calories for each meal
- Include macronutrient breakdown (Protein, Carbs, Fat)
- Ensure meals match dietary preference
- Keep plan practical and realistic

Output Format:
Breakfast:
Lunch:
Dinner:
Snacks:
with calories and macronutrient breakdown.
""",
    input_variables=["age","weight","height","activity","diet","goal"]
)


fitness_prompt = PromptTemplate(
    template="""
You are a professional fitness coach AI.

Create a personalized workout plan based on:
Age: {age}
Weight: {weight}
Height: {height}
Activity Level: {activity}
Fitness Goal: {goal}

Requirements:
- Include warm-up
- Main workout
- Cool-down
- Sets/Reps
- Rest days
- Beginner friendly

Output Format:
Warm-Up:
Workout Plan:
Cool-Down:
Rest Days:
Trainer Tips:
""",
    input_variables=["age","weight","height","activity","diet","goal"]
)


weekly_prompt = PromptTemplate(
    template="""
You are a holistic health planner AI.

Meal Plan:
{meal_plan}

Fitness Plan:
{fitness_plan}

Create a structured weekly schedule.

Requirements:
- 7 day plan
- Meals + workouts
- Hydration target
- Sleep hours
- Daily motivation tip

Output Format:
Weekly Summary:
""",
    input_variables=["meal_plan","fitness_plan"]
)
