class SkillMatcher:
    def _init_(self):
        self.teachers = []
        self.learners = []
    
    def add_teacher(self, teacher_id, skills, location, availability):
        """Add teacher to matching pool"""
        teacher = {
            'id': teacher_id,
            'skills': skills,
            'location': location,
            'availability': availability,
            'rating': 4.5  # Default rating
        }
        self.teachers.append(teacher)
        return teacher
    
    def add_learner(self, learner_id, desired_skills, location):
        """Add learner to matching pool"""
        learner = {
            'id': learner_id,
            'desired_skills': desired_skills,
            'location': location
        }
        self.learners.append(learner)
        return learner
    
    def find_matches(self, learner_id, desired_skill, max_distance_km=10):
        """Find compatible teachers for a learner"""
        learner = next((l for l in self.learners if l['id'] == learner_id), None)
        if not learner:
            return []
            
        matches = []
        
        for teacher in self.teachers:
            if desired_skill in teacher['skills']:
                distance = self.calculate_distance(learner['location'], teacher['location'])
                
                if distance <= max_distance_km:
                    match_score = self.calculate_match_score(teacher, desired_skill, distance)
                    
                    matches.append({
                        'teacher_id': teacher['id'],
                        'skill': desired_skill,
                        'distance_km': round(distance, 2),
                        'match_score': round(match_score, 2),
                        'availability': teacher['availability'],
                        'rating': teacher['rating']
                    })
        
        return sorted(matches, key=lambda x: x['match_score'], reverse=True)
    
    def calculate_distance(self, loc1, loc2):
        """Calculate distance between two locations (simplified Haversine)"""
        # Simplified distance calculation for demo
        # In production, this would use proper geolocation
        return abs(loc1 - loc2) * 100  # Convert to approximate km
    
    def calculate_match_score(self, teacher, skill, distance):
        """Calculate overall match score (0-100)"""
        skill_match = 80  # Base score for skill match
        proximity_score = max(0, 100 - (distance * 2))  # Deduct for distance
        rating_score = teacher['rating'] * 15  # Weight rating heavily
        
        return (skill_match + proximity_score + rating_score) / 3

# Example usage
if _name_ == "_main_":
    matcher = SkillMatcher()
    
    # Add some sample teachers
    matcher.add_teacher("teacher1", ["python", "javascript"], 6.5244, "Weekends")
    matcher.add_teacher("teacher2", ["python", "react"], 6.5245, "Evenings")
    matcher.add_teacher("teacher3", ["javascript", "vue"], 6.6000, "Weekdays")
    
    # Add a learner
    matcher.add_learner("learner1", ["python"], 6.5244)
    
    # Find matches
    matches = matcher.find_matches("learner1", "python")
    
    print("Skill Matching Results:")
    print("=" * 50)
    for match in matches:
        print(f"Teacher: {match['teacher_id']}")
        print(f"Skill: {match['skill']}")
        print(f"Distance: {match['distance_km']}km")
        print(f"Match Score: {match['match_score']}/100")
        print(f"Availability: {match['availability']}")
        print("-" * 30)
