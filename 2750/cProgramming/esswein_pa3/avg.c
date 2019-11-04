float avg(float *a, float N){
    float sum;
    for(int i = 0; i < N; i++){
        sum +=a[i];
    }
    
    float avg = (sum / 10);

    return avg;
}
