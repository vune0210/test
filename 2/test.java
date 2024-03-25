import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;



import static java.lang.Integer.min;
import static java.lang.Math.max;

public class fun_schedule {
    /**
     * sắp xếp danh sách các tiến trình theo trình tự tới hàng đợi để đến cpu
     */
    static Comparator<Process> comparator_at = new Comparator<Process>() {
        @Override
        public int compare(Process x1, Process x2) {
            return Integer.compare(x1.getArrivalTime(), x2.getArrivalTime());
        }
    };

    public static List<Process> myInput(String s) {
        File myfile = new File(s);
        Scanner sc = null;
        try {
            sc = new Scanner(myfile);
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
        d
        int n;
        System.out.println("Đã nhận vào số n");
        n = sc.nextInt();
        List<Process> p = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            Process t_prc = new Process(sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt());
            t_prc.setRemaining_time(t_prc.getBurstTime());// sử dụng cho các trường hợp cho phép dừng.
            System.out.println("Đã nhận thông số của P[" + t_prc.getProcessId() + "]");
            p.add(t_prc);
        }
        return p;
    }
    abstract
}