class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_of_students_not_able_to_eat = len(students)
        count = Counter(students) # count the occurrences and store in hash map

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                num_of_students_not_able_to_eat -=1
                count[sandwich] -=1
            else:
                break
        
        return num_of_students_not_able_to_eat
            
