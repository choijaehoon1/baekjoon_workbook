import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static int M,N,K;
	public static int[][] visit;
	public static int[][] board;
	public static int[] dx = {-1,1,0,0};
	public static int[] dy = {0,0,-1,1};

	public static void bfs(int x, int y, int cnt) {
		Queue<int[]> q = new LinkedList<int[]>();
		q.offer(new int[] {x,y});
		visit[x][y] = 1;
		
		while(!q.isEmpty()) {
			int[] t = q.poll();
			x = t[0];
			y = t[1];
			for(int k=0; k<4;k++) {
				int nx = dx[k] + x;
				int ny = dy[k] + y;
				if(nx>=0 && nx<N && ny>=0 && ny>=0 && ny<M) {
					if (visit[nx][ny] == 0 && board[nx][ny] == -1) {
						visit[nx][ny] = 1;
						board[nx][ny] = cnt;
						q.offer(new int[] {nx,ny});
								
					}
					
				} 
				
			}
			
		}
		
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine());
		
		
		for(int t=0; t<tc; t++) {
			StringTokenizer stz = new StringTokenizer(br.readLine()," ");
			M = Integer.parseInt(stz.nextToken());
			N = Integer.parseInt(stz.nextToken());
			K = Integer.parseInt(stz.nextToken());
			board = new int[N][M];
			visit = new int[N][M];
			for(int i=0; i<K; i++) {
				stz = new StringTokenizer(br.readLine()," ");
				int X = Integer.parseInt(stz.nextToken());
				int Y = Integer.parseInt(stz.nextToken());
				board[Y][X] = -1;
			}
			
			int cnt = 0;
			for(int i=0; i<N;i++) {
				for(int j=0; j<M;j++) {
					if(board[i][j] == -1) {
						cnt += 1;
						bfs(i,j,cnt);
					}
					
				}
			}
			System.out.println(cnt);
		}
		
	}

}
