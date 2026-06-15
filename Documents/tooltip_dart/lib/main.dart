import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Tooltip Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF2563EB),
          brightness: Brightness.light,
        ),
        useMaterial3: true,
        inputDecorationTheme: InputDecorationTheme(
          filled: true,
          fillColor: const Color(0xFFF8FAFC),
          contentPadding:
          const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(10),
            borderSide: const BorderSide(color: Color(0xFFE2E8F0)),
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(10),
            borderSide: const BorderSide(color: Color(0xFFE2E8F0)),
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(10),
            borderSide: const BorderSide(color: Color(0xFF2563EB), width: 1.8),
          ),
          labelStyle: const TextStyle(color: Color(0xFF64748B)),
        ),
      ),
      home: const SignUpPage(),
    );
  }
}

class SignUpPage extends StatelessWidget {
  const SignUpPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF1F5F9),
      body: Center(
        child: SingleChildScrollView(
          child: Container(
            width: 480,
            margin: const EdgeInsets.symmetric(horizontal: 24, vertical: 40),
            padding: const EdgeInsets.all(36),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(16),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withOpacity(0.07),
                  blurRadius: 24,
                  offset: const Offset(0, 8),
                ),
              ],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // ── Header ──────────────────────────────────────────
                Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.all(10),
                      decoration: BoxDecoration(
                        color: const Color(0xFFEFF6FF),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: const Icon(
                        Icons.person_add_outlined,
                        color: Color(0xFF2563EB),
                        size: 22,
                      ),
                    ),
                    const SizedBox(width: 14),
                    const Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Create Account',
                          style: TextStyle(
                            fontSize: 20,
                            fontWeight: FontWeight.w700,
                            color: Color(0xFF0F172A),
                          ),
                        ),
                        Text(
                          'Fill in the details below to get started',
                          style: TextStyle(
                            fontSize: 13,
                            color: Color(0xFF64748B),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),

                const SizedBox(height: 32),
                const _SectionLabel(text: 'ACCOUNT DETAILS'),
                const SizedBox(height: 12),

                // ── Username — shows: message property ──────────────
                _TooltipField(
                  label: 'Username',
                  icon: Icons.person_outline,
                  tooltipMessage:
                  'Must be 6–20 characters.\nOnly letters, numbers, and underscores.',
                  preferBelow: true,
                ),

                const SizedBox(height: 16),

                // ── Password — shows: preferBelow: false ────────────
                _TooltipField(
                  label: 'Password',
                  icon: Icons.lock_outline,
                  tooltipMessage:
                  'Min 8 characters.\nRequires uppercase, number & special character.',
                  preferBelow: false,
                  obscureText: true,
                ),

                const SizedBox(height: 32),
                const _SectionLabel(text: 'CONTACT'),
                const SizedBox(height: 12),

                // ── Email — shows: decoration property ─────────────
                _TooltipField(
                  label: 'Email Address',
                  icon: Icons.email_outlined,
                  tooltipMessage:
                  'We\'ll send a confirmation link here.\nMust be a valid email address.',
                  preferBelow: true,
                  useCustomDecoration: true,
                ),

                const SizedBox(height: 32),

                // ── Submit button ───────────────────────────────────
                SizedBox(
                  width: double.infinity,
                  child: FilledButton(
                    onPressed: () {},
                    style: FilledButton.styleFrom(
                      backgroundColor: const Color(0xFF2563EB),
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10),
                      ),
                    ),
                    child: const Text(
                      'Create Account',
                      style: TextStyle(
                        fontSize: 15,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                ),

                const SizedBox(height: 16),

                // ── Sign in link ────────────────────────────────────
                Center(
                  child: RichText(
                    text: const TextSpan(
                      text: 'Already have an account? ',
                      style: TextStyle(
                        color: Color(0xFF64748B),
                        fontSize: 13,
                      ),
                      children: [
                        TextSpan(
                          text: 'Sign in',
                          style: TextStyle(
                            color: Color(0xFF2563EB),
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}


class _SectionLabel extends StatelessWidget {
  final String text;
  const _SectionLabel({required this.text});

  @override
  Widget build(BuildContext context) {
    return Text(
      text,
      style: const TextStyle(
        fontSize: 11,
        fontWeight: FontWeight.w700,
        letterSpacing: 1.2,
        color: Color(0xFF94A3B8),
      ),
    );
  }
}


class _TooltipField extends StatelessWidget {
  final String label;
  final IconData icon;
  final String tooltipMessage;
  final bool preferBelow;
  final bool obscureText;
  final bool useCustomDecoration;

  const _TooltipField({
    required this.label,
    required this.icon,
    required this.tooltipMessage,
    this.preferBelow = true,
    this.obscureText = false,
    this.useCustomDecoration = false,
  });

  @override
  Widget build(BuildContext context) {
    return TextField(
      obscureText: obscureText,
      decoration: InputDecoration(
        labelText: label,
        prefixIcon: Icon(icon, size: 18, color: const Color(0xFF94A3B8)),
        suffixIcon: Tooltip(
          message: tooltipMessage,       // Property 1: message
          preferBelow: preferBelow,      // Property 2: preferBelow
          decoration: useCustomDecoration // Property 3: decoration
              ? BoxDecoration(
            color: const Color(0xFF1E3A5F),
            borderRadius: BorderRadius.circular(10),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withOpacity(0.2),
                blurRadius: 8,
                offset: const Offset(0, 4),
              ),
            ],
          )
              : null,
          textStyle: useCustomDecoration
              ? const TextStyle(
            color: Colors.white,
            fontSize: 13,
            height: 1.5,
          )
              : null,
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
          child: Icon(
            Icons.info_outline,
            size: 18,
            color: const Color(0xFF2563EB).withOpacity(0.7),
          ),
        ),
      ),
    );
  }
}