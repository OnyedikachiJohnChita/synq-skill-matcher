class CompatibilityCalculator:
    def _init_(self):
        self.skill_weights = {
            'programming': 1.2,
            'design': 1.1,
            'business': 1.0,
            'language': 1.3,
            'music': 1.0,
            'sports': 1.0
        }
    
    def calculate_skill_compatibility(self, teacher_skills, learner_desired_skills):
        """Calculate skill compatibility score between teacher and learner"""
        common_skills = set(teacher_skills) & set(learner_desired_skills)
        
        if not common_skills:
            return 0
        
        total_score = 0
        for skill in common_skills:
            skill_type = self.categorize_skill(skill)
            weight = self.skill_weights.get(skill_type, 1.0)
            total_score += 100 * weight
        
        return total_score / len(common_skills)
    
    def categorize_skill(self, skill):
        """Categorize skill into broad categories for weighting"""
        programming_skills = ['python', 'javascript', 'java', 'react', 'nodejs', 'html', 'css']
        design_skills = ['photoshop', 'figma', 'ui/ux', 'graphic design']
        language_skills = ['english', 'french', 'spanish', 'german']
        
        if skill.lower() in programming_skills:
            return 'programming'
        elif skill.lower() in design_skills:
            return 'design'
        elif skill.lower() in language_skills:
            return 'language'
        else:
            return 'general'
    
    def calculate_schedule_compatibility(self, teacher_availability, learner_preferred_times):
        """Calculate how well schedules match"""
        teacher_slots = self.parse_availability(teacher_availability)
        learner_slots = self.parse_availability(learner_preferred_times)
        
        matching_slots = set(teacher_slots) & set(learner_slots)
        
        if not teacher_slots:
            return 0
        
        return (len(matching_slots) / len(teacher_slots)) * 100
    
    def parse_availability(self, availability_str):
        """Parse availability string into time slots"""
        # Simplified parsing - in real app would use proper datetime
        slots = []
        if 'weekend' in availability_str.lower():
            slots.extend(['saturday', 'sunday'])
        if 'weekday' in availability_str.lower():
            slots.extend(['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
        if 'evening' in availability_str.lower():
            slots.append('evening')
        if 'morning' in availability_str.lower():
            slots.append('morning')
        
        return slots if slots else ['flexible']

# Example usage
if _name_ == "_main_":
    calculator = CompatibilityCalculator()
    
    # Test skill compatibility
    teacher_skills = ["python", "javascript", "react"]
    learner_desired = ["python", "nodejs"]
    
    score = calculator.calculate_skill_compatibility(teacher_skills, learner_desired)
    print(f"Skill Compatibility Score: {score:.2f}")
    
    # Test schedule compatibility
    teacher_avail = "Weekends and Evenings"
    learner_pref = "Weekends"
    
    schedule_score = calculator.calculate_schedule_compatibility(teacher_avail, learner_pref)
    print(f"Schedule Compatibility Score: {schedule_score:.2f}")
