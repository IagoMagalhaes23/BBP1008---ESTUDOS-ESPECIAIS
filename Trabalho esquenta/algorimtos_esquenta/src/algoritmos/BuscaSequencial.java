package algoritmos;

public class BuscaSequencial {

	public static int buscaSequencial_v1(int x, int v[]) {

		int indice=-1;
		for (int i = 0; i < v.length; i++) {
			if (v[i] == x)
			   indice = i;
		}
		return indice;
	}
	
	public static int buscaSequencial_v2(int x, int v[]) {

		for (int i = 0; i < v.length; i++) {
			if (v[i] == x)
				return i;
		}
		return -1;
	}


	public static void main(String[] args) {
		int vet[] = { 2, 4, 5, 6, 2, 4, 9, 4, 5, 6 };
		
		System.out.println(buscaSequencial_v1(6, vet));
		System.out.println(buscaSequencial_v2(6, vet));
	}
}
