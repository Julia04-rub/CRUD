import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Tooltip Demo',
      theme: ThemeData(primarySwatch: Colors.indigo),
      home: const SignUpForm(),
    );
  }
}

class SignUpForm extends StatelessWidget {
  const SignUpForm({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Create Account')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // 1. Basic tooltip — message property
            _FormRowWithTooltip(
              label: 'Username',
              tooltipMessage: 'Must be 6–20 characters. No spaces.',
              preferBelow: true, // property 2
            ),

            const SizedBox(height: 24),

            // 2. Tooltip above the icon
            _FormRowWithTooltip(
              label: 'Password',
              tooltipMessage: 'Min 8 chars, one uppercase, one number.',
              preferBelow: false,
            ),

            const SizedBox(height: 24),

            // 3. Custom styled tooltip — decoration property
            _FormRowWithTooltip(
              label: 'Email',
              tooltipMessage: 'We\'ll send a confirmation link here.',
              preferBelow: true,
              customDecoration: BoxDecoration(
                color: Colors.indigo.shade700,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: Colors.white24),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _FormRowWithTooltip extends StatelessWidget {
  final String label;
  final String tooltipMessage;
  final bool preferBelow;
  final Decoration? customDecoration;

  const _FormRowWithTooltip({
    required this.label,
    required this.tooltipMessage,
    this.preferBelow = true,
    this.customDecoration,
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: TextField(
            decoration: InputDecoration(
              labelText: label,
              border: const OutlineInputBorder(),
            ),
          ),
        ),
        const SizedBox(width: 8),
        Tooltip(
          message: tooltipMessage,         // Property 1: message
          preferBelow: preferBelow,        // Property 2: preferBelow
          decoration: customDecoration,    // Property 3: decoration
          child: const Icon(Icons.info_outline, color: Colors.indigo),
        ),
      ],
    );
  }
}