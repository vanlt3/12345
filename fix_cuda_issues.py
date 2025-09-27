#!/usr/bin/env python3
"""
Fix CUDA/TensorFlow registration issues
"""

import os
import warnings

def fix_cuda_registration_issues():
    """
    Fix CUDA factory registration conflicts
    """
    print("🔧 Fixing CUDA registration issues...")
    
    # Suppress CUDA warnings
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Use only first GPU
    
    # Suppress specific warnings
    warnings.filterwarnings('ignore', category=UserWarning)
    warnings.filterwarnings('ignore', message='.*cuFFT factory.*')
    warnings.filterwarnings('ignore', message='.*cuDNN factory.*')
    warnings.filterwarnings('ignore', message='.*cuBLAS factory.*')
    warnings.filterwarnings('ignore', message='.*computation placer already registered.*')
    
    # Set TensorFlow configuration
    os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
    os.environ['TF_GPU_THREAD_MODE'] = 'gpu_private'
    
    print("✅ CUDA registration issues fixed")

def fix_tensorflow_config():
    """
    Configure TensorFlow to avoid conflicts
    """
    print("🔧 Configuring TensorFlow...")
    
    try:
        import tensorflow as tf
        
        # Configure GPU memory growth
        gpus = tf.config.experimental.list_physical_devices('GPU')
        if gpus:
            try:
                for gpu in gpus:
                    tf.config.experimental.set_memory_growth(gpu, True)
                print("✅ GPU memory growth configured")
            except RuntimeError as e:
                print(f"⚠️ GPU configuration warning: {e}")
        
        # Set thread configuration
        tf.config.threading.set_inter_op_parallelism_threads(0)
        tf.config.threading.set_intra_op_parallelism_threads(0)
        
        print("✅ TensorFlow configuration completed")
        
    except ImportError:
        print("⚠️ TensorFlow not available, skipping configuration")

if __name__ == "__main__":
    fix_cuda_registration_issues()
    fix_tensorflow_config()