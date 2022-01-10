import queue as q

def inputan_data (n) :
    task = []
    for i in range (n) :
        a = input("Nama Proses Ke- () : " .format(i).upper)
        b = int(input("Waktu Proses :"))
        task.append [a,b]
    return task

def schedulling(limitTime,task) :
    data = q.createQueue ()
    for i in task:
        q.enqueue(data,i)
        print("Waktu Proses = " ,limitTime)
        print("Antrian Proses Beserta Waktunya = " ,data)
    cont = 1
    while not q.isEmpty(data) :
        ("Iterasi Ke- " ,cont)
        cont += 1
        temp = q.dequeue(data)
        pengurangan_W = temp[1] - limitTime
        if pengurangan_W > 0:
            q.enqueue(data,temp)
            data[0] [1] = pengurangan_W
            print("\tProses {} Sedang di proses, sisa waktu Proses {} = {} " ,format(temp(0),temp(0),pengurangan_W))     
        else :
            print("\tProses {} Telah seslesai di Proses" .format(temp[0]))

        print("\tData Yang Tersisa" ,data) 

w = 3
print("Jumlah Proses Yang akan Di jadwal di CPU", w)
x =inputan_data(3)
schedulling(w,x)

