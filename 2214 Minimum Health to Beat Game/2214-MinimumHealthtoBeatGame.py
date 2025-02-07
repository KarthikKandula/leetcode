class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # variable to store max damage
        maxDamage = 0
        # variable to store total damage
        total = 0

        # loop for each damage
        for n in damage:
            total += n # add current number to total
            maxDamage = max(maxDamage, n) # get max damage
        
        # get the max damage this armor can save
        maxArmorSave = min(maxDamage, armor)

        # return the value of total subtracted by the max armor saved 
        # add 1 since at least 1 health should be remaining by the end
        return total - maxArmorSave + 1
