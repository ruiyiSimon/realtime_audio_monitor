# Real-time Audio Monitor

实时音频信号采集、频谱分析与异常告警系统。

基于麦克风采集环境音频，完成时域波形分析、RMS 能量计算、FFT 频谱分析，
并可对噪声/异响进行阈值检测与告警记录。项目用于学习《信号与系统》《数字信号处理》，
同时可作为环境噪音、设备异响的监测工具。

## 目录

- [功能](#功能)
- [工作原理](#工作原理)
- [技术栈](#技术栈)
- [目录结构](#目录结构)
- [环境要求](#环境要求)
- [安装](#安装)
- [使用](#使用)
- [配置](#配置)
- [开发计划](#开发计划)
- [作者](#作者)

## 功能

- [x] 实时麦克风音频采集（可配置采样率、块大小）
- [x] 滑动平均滤波，平滑信号
- [x] RMS 信号能量计算
- [x] FFT 频谱分析，提取主频
- [ ] 阈值告警（弹窗/提示）
- [ ] 异常事件写入 CSV 日志
- [ ] 分频段能量检测
- [ ] 实时波形/频谱可视化 GUI

## 工作原理

```
麦克风采集 → 滑动平均滤波 → RMS 能量 / FFT 频谱 → 主频提取 → (告警 + 日志)
```

- **采样**：采样率 `fs` 需大于信号最高频率 2 倍，防止频谱混叠。
- **RMS**：`RMS = sqrt(1/N * Σx²)`，代表信号有效能量。
- **FFT**：将时域信号分解为不同频率分量，得到频谱。
- **频率分辨率**：`Δf = fs / N`，决定 FFT 能分辨的最小频率间隔。

## 技术栈

- Python 3.12
- sounddevice — 音频采集
- numpy — 数值计算与 FFT

## 目录结构

```
realtime_audio_monitor/
├─ config.json          # 采样率、阈值等参数
├─ requirements.txt     # 依赖清单
├─ src/
│  ├─ main.py           # 主程序入口
│  ├─ acquisition.py    # 麦克风采集
│  ├─ dsp.py            # RMS / 滑动平均 / FFT
│  └─ config.py         # 配置读取
└─ logs/                # 告警日志（运行时生成）
```

## 环境要求

- Python 3.10+
- 可用的麦克风设备

## 安装

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## 使用

```bash
python src/main.py
```

运行后对着麦克风发声，终端会实时打印 `RMS 与主频`，按 `Ctrl+C` 停止：

```
RMS=0.0000  主频=0.0 Hz
RMS=0.1464  主频=516.8 Hz
```

## 配置

参数集中在 `config.json`，修改即可生效，无需改代码：

```json
{
  "audio": { "sample_rate": 44100, "block_size": 2048, "channels": 1 },
  "filter": { "moving_average_window": 5 },
  "detection": { "rms_threshold": 0.05 }
}
```

## 开发计划

- [x] 实时音频采集
- [x] 滑动平均滤波
- [x] RMS 能量计算
- [x] FFT 主频分析
- [ ] 阈值告警
- [ ] CSV 日志记录
- [ ] 分频段能量检测
- [ ] 实时可视化 GUI

## 作者

ruiyiSimon
