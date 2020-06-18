class CustomPager:
    # 클래스변수
    # number=1

    # 멤버 변수
    # 생성자
    # self  ->  this
    def __init__(self, page, kind, search):
        # 멤버 변수 선언
        self.page = page
        self.kind = kind
        self.search = search
        self.startNum = 1
        self.lastNum = 2
        self.range = range(1,2)
        # 이전 블럭 유무
        self.pre = False
        self.next = True

    def makePage(self, totalPage):
        # 한 페이지 당 보여줄 글의 갯수
        perPage = 2

        # 한 블럭 당 출력할 번호의 갯수
        perBlock = 2

        # 전체 블럭
        # //    : 몫만 표시 (정수로 나타내기)
        totalBlock = totalPage // perPage
        if totalPage % perPage != 0 :
            totalBlock += 1

        # page 번호로 현재 블럭 번호 계산
        curBlock = self.page // perBlock
        if self.page % perBlock != 0 :
            curBlock += 1
        
        #curBlock으로 startNum, lastNum 구하기
        self.startNum = (curBlock-1)*perBlock+1
        self.lastNum = curBlock*perBlock

        if curBlock == totalBlock :
            self.lastNum = totalPage
            self.next = False

        # range 는 start 이상 last 미만이므로 +1
        self.lastNum = self.lastNum+1
        self.range = range(self.startNum, self.lastNum)

        # 현재 블럭이 1보다 크면 이전 블럭을 포함
        if curBlock>1 :
            self.pre = True
            self.startNum = self.startNum-1
        