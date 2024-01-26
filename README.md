# jandialgo
This is an auto push repository for Baekjoon 
Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

이중 False를 통해 왔던 길을 돌아가는 최단경로
str.zfill(n) n자릿까지 남은 인덱스에 0을 채움
대각선 확인
(i+j) 인경우는 / 대각선
(i-j) 인 경우는 \ 대각선

대각선 확인 배열은 2n-1크기 왜냐하면 대각선을 그어보면
2n-1개가 존재할 뿐더러 대각선 별로 구해보면
/의 경우 0부터 2n-1까지 값을 가지고
\의 경우 -는-(n-1) 부터 (n-1)까지의 값을 가짐
백트레킹의 핵심은 원래 상태로 되돌려 놓는 것
