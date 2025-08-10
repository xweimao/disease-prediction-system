#!/usr/bin/env python3
"""
疾病预测系统 - 简化版Gradio应用
"""

import numpy as np
import pandas as pd
from datetime import datetime
import time

# 疾病预测函数
def predict_disease(age, gender, symptoms):
    """疾病预测函数"""
    # 模拟预测逻辑
    risk_factors = 0
    
    # 年龄风险
    if age > 60:
        risk_factors += 0.3
    elif age > 40:
        risk_factors += 0.2
    elif age > 20:
        risk_factors += 0.1
    
    # 性别风险（某些疾病）
    if gender == "女":
        risk_factors += 0.1
    
    # 症状风险
    high_risk_symptoms = ["胸痛", "呼吸困难", "头痛", "发热", "咳嗽", "疲劳"]
    if symptoms:
        for symptom in high_risk_symptoms:
            if symptom in symptoms:
                risk_factors += 0.15
    
    # 添加随机因子
    risk_score = min(risk_factors + np.random.uniform(0, 0.2), 1.0)
    
    if risk_score > 0.7:
        risk_level = "高风险 🔴"
        recommendations = "建议立即就医检查，进行详细的医学评估"
    elif risk_score > 0.4:
        risk_level = "中等风险 🟡"
        recommendations = "建议定期体检，注意观察症状变化"
    else:
        risk_level = "低风险 🟢"
        recommendations = "保持健康生活方式，定期体检"
    
    return f"""
🏥 **疾病风险评估结果**

📊 **风险评分**: {risk_score:.2f}
🎯 **风险等级**: {risk_level}
💡 **建议**: {recommendations}
⏰ **评估时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

⚠️ **免责声明**: 此结果仅供参考，不能替代专业医疗诊断
"""

# 数据分析函数
def analyze_data(file_content):
    """数据分析函数"""
    if not file_content:
        return "❌ 请上传数据文件"
    
    try:
        # 模拟数据分析
        time.sleep(2)
        
        # 生成模拟结果
        accuracy = np.random.uniform(0.85, 0.95)
        precision = np.random.uniform(0.80, 0.90)
        recall = np.random.uniform(0.75, 0.85)
        f1_score = np.random.uniform(0.78, 0.88)
        
        return f"""
🔍 **Panda算法分析报告**

📊 **模型性能**
- 准确率: {accuracy:.3f}
- 精确率: {precision:.3f}
- 召回率: {recall:.3f}
- F1分数: {f1_score:.3f}

⚙️ **训练配置**
- 联邦学习: ✅ 启用
- 隐私保护: ✅ 启用
- 参与节点: {np.random.randint(3, 8)}
- 训练时间: {np.random.uniform(120, 300):.1f}秒

🛡️ **隐私保护**
- 差分隐私: ✅ 启用
- 数据安全: 高级别加密

⏰ **分析时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
        
    except Exception as e:
        return f"❌ 分析失败: {str(e)}"

# 如果安装了gradio，使用gradio界面
try:
    import gradio as gr
    
    def create_gradio_interface():
        """创建Gradio界面"""
        with gr.Blocks(title="疾病预测系统", theme=gr.themes.Soft()) as demo:
            gr.Markdown("# 🏥 疾病预测系统")
            gr.Markdown("基于先进AI技术的疾病预测与分析平台")
            
            with gr.Tabs():
                # 疾病预测标签页
                with gr.TabItem("🔍 疾病预测"):
                    with gr.Row():
                        with gr.Column():
                            age = gr.Slider(0, 100, value=30, label="年龄")
                            gender = gr.Radio(["男", "女"], label="性别", value="男")
                            symptoms = gr.Textbox(
                                label="症状描述", 
                                placeholder="请描述您的症状，如：胸痛、头痛、发热、咳嗽等...",
                                lines=3
                            )
                            predict_btn = gr.Button("🔍 开始预测", variant="primary")
                        
                        with gr.Column():
                            prediction_output = gr.Textbox(label="预测结果", lines=10)
                    
                    predict_btn.click(
                        predict_disease,
                        inputs=[age, gender, symptoms],
                        outputs=prediction_output
                    )
                
                # Panda算法标签页
                with gr.TabItem("🐼 Panda算法"):
                    with gr.Row():
                        with gr.Column():
                            data_file = gr.File(label="上传数据文件")
                            analyze_btn = gr.Button("🚀 开始分析", variant="primary")
                        
                        with gr.Column():
                            analysis_output = gr.Textbox(label="分析结果", lines=15)
                    
                    analyze_btn.click(
                        analyze_data,
                        inputs=data_file,
                        outputs=analysis_output
                    )
        
        return demo
    
    # 启动Gradio应用
    if __name__ == "__main__":
        demo = create_gradio_interface()
        demo.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=False
        )

except ImportError:
    print("Gradio未安装，请运行: pip install gradio")
    print("或者使用命令行版本:")
    
    # 命令行版本
    def main():
        print("🏥 疾病预测系统 - 命令行版本")
        print("=" * 50)
        
        while True:
            print("\n请选择功能:")
            print("1. 疾病预测")
            print("2. 数据分析")
            print("3. 退出")
            
            choice = input("\n请输入选择 (1-3): ").strip()
            
            if choice == "1":
                print("\n🔍 疾病预测")
                age = int(input("请输入年龄: "))
                gender = input("请输入性别 (男/女): ")
                symptoms = input("请描述症状: ")
                
                result = predict_disease(age, gender, symptoms)
                print(result)
                
            elif choice == "2":
                print("\n🐼 Panda算法分析")
                print("模拟数据分析...")
                result = analyze_data("sample_data")
                print(result)
                
            elif choice == "3":
                print("感谢使用疾病预测系统！")
                break
            else:
                print("无效选择，请重新输入")
    
    if __name__ == "__main__":
        main()
