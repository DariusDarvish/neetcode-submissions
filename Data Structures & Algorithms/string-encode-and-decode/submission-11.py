class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "Trap"
        return "BadCode".join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="Trap":
            return []
        return s.split("BadCode")
