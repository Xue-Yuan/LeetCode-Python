from typing import List


class Solution:
    '''Use bitmask to represent skills. Do memoization.
    '''

    def smallestSufficientTeam(self, req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        skill_index = {v: i for i, v in enumerate(req_skills)}
        memo = {0: []}

        def getPeopleSkill(p: List[str]) -> int:
            cur_skill = 0
            for skill in p:
                if skill in skill_index:
                    cur_skill |= 1 << skill_index[skill]
            return cur_skill

        def search(remaining_skills: int) -> List[int]:
            if remaining_skills in memo:
                return memo[remaining_skills]
            can = []
            for i, p in enumerate(people):
                cur_skill = getPeopleSkill(p)
                can_provide = remaining_skills & cur_skill
                if can_provide == 0:
                    continue
                tmp = search(remaining_skills - can_provide)
                if not can or len(can) > len(tmp) + 1:
                    can = [i] + tmp
            memo[remaining_skills] = can
            return can

        n = len(req_skills)
        return search((1 << n) - 1)
