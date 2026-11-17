100 epochs completed in 0.029 hours.
Optimizer stripped from C:\Users\User\runs\detect\train-4\weights\last.pt, 5.5MB
Optimizer stripped from C:\Users\User\runs\detect\train-4\weights\best.pt, 5.5MB

Validating C:\Users\User\runs\detect\train-4\weights\best.pt...
Ultralytics 8.4.212  Python-3.13.16 torch-2.14.1+cu130 CUDA:0 (NVIDIA GeForce RTX 5060 Ti, 16283MiB)
YOLO11n summary (fused): 101 layers, 2,597,051 parameters, 0 gradients, 6.4 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP…: 100% ━━━━━━━━━━━━ 1/1 3.1it/s 0.3s
                   all         20         20      0.997          1      0.995       0.99
Speed: 0.1ms preprocess, 1.2ms inference, 0.0ms loss, 0.6ms postprocess per image
Results saved to C:\Users\User\runs\detect\train-4
 Learn more at https://docs.ultralytics.com/modes/train

(lebel) C:\Users\User>yolo detect predict model="C:\Users\User\runs\detect\train-4\weights\best.pt" source="C:\Users\User\Desktop\mushroom_dataset\images\val" save=True
Ultralytics 8.4.212  Python-3.13.16 torch-2.14.1+cu130 CUDA:0 (NVIDIA GeForce RTX 5060 Ti, 16283MiB)
YOLO11n summary (fused): 101 layers, 2,597,051 parameters, 0 gradients, 6.4 GFLOPs