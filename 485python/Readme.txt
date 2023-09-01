s -> 태양광 단상
shf -> 태양열 강제 순환
gt -> 지열


파이썬 코드 열어서 com포트 적어주시면 됩니다.


s -> 단상 국번 1
shf_1 -> 생산측 국번 1
shf_2 -> 부하측 국번 3
gt_1 -> 지열 히트펌프 국번 1
gt_2 -> 지열 부하측 국번 2
gt_3 -> 지열 축열조 국번4


python3 설치 후 pyserial 설치하시면 됩니다.
pip install pyserial

이후 스크립트 python s_1.py 으로 실행하면 됩니다.