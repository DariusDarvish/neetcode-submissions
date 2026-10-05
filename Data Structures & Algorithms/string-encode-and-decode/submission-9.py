class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "Trap"
        return "poopoo".join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="Trap":
            return []
        return s.split("poopoo")
