# Synq Skill Matcher 🤝

Advanced skill matching algorithm for the Synq platform. This system intelligently connects teachers and learners based on skill compatibility, geographical proximity, and schedule availability.

## 🎯 Features

- *Intelligent Skill Matching*: Finds optimal teacher-learner pairs
- *Proximity-Based Ranking*: Prioritizes nearby matches
- *Schedule Compatibility*: Matches based on availability
- *Rating Integration*: Considers teacher ratings in matching
- *Extensible Architecture*: Easy to add new matching criteria

## 🚀 Quick Start

```python
from skill_matcher import SkillMatcher

# Initialize matcher
matcher = SkillMatcher()

# Add teachers
matcher.add_teacher(
    teacher_id="john_doe",
    skills=["python", "machine learning"],
    location=6.5244,  # Latitude coordinate
    availability="Weekends"
)

# Add learners  
matcher.add_learner(
    learner_id="jane_smith",
    desired_skills=["python"],
    location=6.5245
)

# Find matches
matches = matcher.find_matches("jane_smith", "python")
print(matches)
